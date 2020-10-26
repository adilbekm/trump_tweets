import os
import sys
import time
from datetime import datetime, timezone, timedelta
import json
import urllib.parse as parse
import urllib.request as request
from urllib.error import HTTPError


##### initial setup

b_token = 'abc' # update with actual value

header = {'Authorization': 'Bearer {}'.format(b_token)} 

# twitter api limits:
#   v1: 10 requests per sec, 60 requests per min
#   v2: 300 requests per 15 min
twt_limits = [(10, 1), (60, 60), (300, 900)] 
#   v2 limit for ids per request (max = 100)
ids_lim = 100 

# set endpoint and params
endpt = 'https://api.twitter.com/2/tweets'
twt_flds = [
    'created_at',
    'author_id',
    'source',
    'entities',
    'geo',
    'referenced_tweets',
    'public_metrics']
param = {
    'ids': None,
    'tweet.fields': ','.join(twt_flds)}


##### prepare files

fnames = [
    'trump_twt_small.csv',
    'trump_twt_big.json']

# clean out old files
for f in fnames:
    try: os.remove(f)
    except OSError: pass

# open files
f_ids = open('trump_twt_ids.csv', 'r', encoding='utf8')
f_small = open(fnames[0], 'a', encoding='utf8')
f_big= open(fnames[1], 'a', encoding='utf8')

# make header for brief csv file
cols_small = ['id', 'author_id', 'created_at', 'source', 'text']
f_small.write(','.join(cols_small) + '\n')


##### utilities

class LimitsTracker:
    '''Class for managing twitter api limits.
    Provide limits at object initiation as list of tuples [(r, t)...]
    where r is number of requests and t is time in seconds. For example,
    (10, 1) represents a limit of 10 requests per second.
   '''
    def _now(self):
        return datetime.now(timezone.utc)

    def __init__(self, limits):
        now = self._now()
        new_limits = []
        for limit in limits: 
            r, t = limit
            new_limits.append((r, timedelta(seconds=t))) 
        self.limits = new_limits
        self.count = [0 for i in range(len(limits))]
        self.prev = [now for i in range(len(limits))]

    def check(self):
        '''Check all limits and delay execution as necessary.
        '''
        delays = []
        for i in range(len(self.limits)):
            delay = 0
            rlimit, tlimit = self.limits[i]
            now = self._now()
            if (now - self.prev[i]) > tlimit:
                self.prev[i] = now
                self.count[i] = 1
            else:
                if self.count[i] < rlimit:
                    self.count[i] += 1
                else:
                    self.count[i] = 1
                    delay = tlimit - (now - self.prev[i])
                    delay = delay.seconds + 5
            delays.append(delay)
        maxdelay = max(delays)
        if maxdelay:
            print('pausing {} secs...'.format(maxdelay))
            time.sleep(maxdelay)
        return

# instantiate trackers
reqs = 0
limits = LimitsTracker(twt_limits)

def get_data(header, endpoint, params, token=None):
    '''Function to fetch twitter data.
    '''
    global reqs
    if token:
        params['next'] = token
    query = parse.urlencode(params)
    url = endpoint + '?' + query
    req = request.Request(url, headers=header)
    limits.check()
    try:
        reqs += 1
        print('making request # {}'.format(reqs))
        res = request.urlopen(req)
    except HTTPError as e:
        print('HTTP error received, stopping...')
        print('code: {}\nreason: {}\nheaders:\n{}'.format(e.code, e.reason, e.headers))
        sys.exit()
    return res

def utc_now():
    return datetime.now(timezone.utc)


##### fetch data

print('begin {}'.format(utc_now()))

# load ids from file
ids = []
for i in f_ids.readlines():
    ids.append(i.strip())

data = []

while len(ids) > 0:
    
    if len(ids) > ids_lim:
        ids_now = ids[:ids_lim]
        ids = ids[ids_lim:]
    else:
        ids_now = ids
        ids = []

    ids_now = ','.join(ids_now)

    param['ids'] = ids_now
    
    res = get_data(header, endpt, param)

    if res.status != 200:
        print('response status {}, stopping...'.format(res.status))
        print(res.read().decode('utf-8'))
        sys.exit()

    rstr = res.read().decode('utf-8') # convert to str
    r = json.loads(rstr) # convert to dict

    data.extend(r['data'])

print('writing data to files') 

# write to small csv file
vals_small = [None for i in cols_small]
for twt in data:
    for i, col in enumerate(cols_small):
        if col in twt:
            vals_small[i] = twt[col].replace('\n', ' ')
    # replace any None's with empty str
    vals = [v if v else '' for v in vals_small]
    f_small.write(','.join(vals) + '\n')

# write to big json file
json.dump(data, f_big, ensure_ascii=False, indent=2, sort_keys=True)


print('total requests made: {}'.format(reqs))
print('end {}'.format(utc_now()))

