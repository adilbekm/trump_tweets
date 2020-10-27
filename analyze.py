import os
import sys
import json
from datetime import datetime, timezone


try: os.remove('trump_tweets.csv')
except OSError: pass

f_csv = open('trump_tweets.csv', 'a', encoding='utf8')
f_json = open('trump_tweets.json', 'r', encoding='utf8')

tweets = json.load(f_json)

total_count = len(tweets)

for t in tweets:
    twt_id = t['id']
    author_id = t['author_id']
    strtime = t['created_et'] # Eastern Time
    created = datetime.fromisoformat(strtime) # to str: .isoformat()
    created_yy = created.year
    created_mm = created.month
    created_hh = created.hour
    source = t['source']
    text = t['text']

    # write tweet to csv file
    flds = [
        twt_id, 
        author_id, 
        created.isoformat(),
        #str(created_yy),
        #str(created_mm),
        #str(created_hh),
        source, 
        text.replace('\n', ' ')
    ]
    f_csv.write(', '.join(flds) + '\n')


# write to file



print('Number of tweets: {}'.format(total_count))


# {'id', 'author_id', 'created_at', 'source', 'public_metrics', 'referenced_tweets', 'entities', 'geo', 'text'}

