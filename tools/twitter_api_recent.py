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
#   v2 search/recent api: 450 requests per 15 min
twt_limits = [(10, 1), (60, 60), (300, 900)] 

# set endpoint and params
endpt = 'https://api.twitter.com/2/tweets/search/recent'
twt_flds = [
    'created_at',
    'author_id',
    'source',
    'entities',
    'geo',
    'referenced_tweets',
    'public_metrics']
param = {
    'query': 'from:25073877',         # trump twitter id
    'max_results': '50',               # 10-100
    'tweet.fields': ','.join(twt_flds)}


##### prepare files

now = datetime.now().strftime('%Y-%m-%d')
fname1 = 'trump_tweets_recent_{}.json'.format(now)
fnames = [fname1]

# clean out old files
for f in fnames:
    try: os.remove(f)
    except OSError: pass

# open files
f_tweets = open(fnames[0], 'a', encoding='utf8')


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

reqs = 0
limits = LimitsTracker(twt_limits)

def get_data(header, endpoint, params, token=None):
    '''Function to fetch twitter data.
    '''
    global reqs
    if token:
        params['next_token'] = token
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

tweets = []
res = get_data(header, endpt, param) 

while True:
    rstr = res.read().decode('utf-8') # convert to str
    r = json.loads(rstr) # convert to dict
    twts = r['data']
    tweets.extend(twts)
    if 'next_token' in r['meta']:
        nexttk = r['meta']['next_token']
        res = get_data(header, endpt, param, nexttk)
    else:
        break

# write to file
json.dump(tweets, f_tweets, ensure_ascii=False, indent=2, sort_keys=True)


print('total requests made: {}'.format(reqs))
print('total tweets fetched: {}'.format(len(tweets)))
print('end {}'.format(utc_now()))

