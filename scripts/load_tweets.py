# Script for loading tweets from json to pandas dataframe

src_filename = 'trump_tweets.json'

import os
import sys
import json
from datetime import datetime, timezone
import numpy as np
import pandas as pd

f_src = open(src_filename, 'r', encoding='utf8')

tweets = json.load(f_src)

tweet_ct = len(tweets) 

df_cols = [
    'id', 
    'created',
    'created_yy',
    'created_mm',
    'created_dd',
    'created_wd', # weekday (monday=0, ..., sunday=6)
    'source', 
    'is_retweet', 
    'retweet_id', 
    'retweet_type', 
    'retweet2_id', 
    'retweet2_type', 
    'retweet_ct', 
    'reply_ct', 
    'like_ct', 
    'quote_ct',
    'text',
    'text_len']

# create empty dataframe 
df = pd.DataFrame(index=np.arange(tweet_ct), columns=df_cols)

for i, t in enumerate(tweets):

    # collect tweet data 
    twt_id = t['id']
    #author_id = t['author_id']
    strtime = t['created_et'] # Eastern Time
    created_et = datetime.fromisoformat(strtime) # to str: .isoformat()
    created = created_et.replace(tzinfo=None) # convert to naive time
    created_yy = created.year
    created_mm = created.month
    created_dd = created.day
    created_wd = created.weekday()
    #created_yy = created.year
    #created_mm = created.month
    #created_hh = created.hour
    source = t['source']
    # trump retweets at most 2 tweets, historically
    rt_id = rt_type = None
    rt2_id = rt2_type = None
    is_retweet = False
    if 'referenced_tweets' in t:
        rt = t['referenced_tweets']
        rt_id, rt_type = rt[0]['id'], rt[0]['type']
        if len(rt) > 1:
            rt2_id, rt2_type = rt[1]['id'], rt[1]['type']
        if rt_type == 'retweeted' or rt2_type == 'retweeted':
            is_retweet = True
    pm = t['public_metrics']
    rt_ct = pm['retweet_count']
    rp_ct = pm['reply_count']
    lk_ct = pm['like_count']
    qt_ct = pm['quote_count']
    text = t['text'] # need to replace \n?
    text_len = len(text)

    # load into dataframe
    df.iloc[i] = [
        twt_id,
        created,
        created_yy,
        created_mm,
        created_dd,
        created_wd,
        source,
        is_retweet,
        rt_id,
        rt_type,
        rt2_id,
        rt2_type,
        rt_ct,
        rp_ct,
        lk_ct,
        qt_ct,
        text,
        text_len]

# change dtypes
df = df.astype({
    'id': 'string', 
    'created': 'datetime64[ns]', 
    'created_yy': 'int64',
    'created_mm': 'int64',
    'created_dd': 'int64',
    'created_wd': 'int64',
    'source': 'string', 
    'is_retweet': 'boolean', 
    'retweet_id': 'string', 
    'retweet_type': 'string', 
    'retweet2_id': 'string', 
    'retweet2_type': 'string', 
    'retweet_ct': 'int64', 
    'reply_ct': 'int64', 
    'like_ct': 'int64', 
    'quote_ct': 'int64',
    'text': 'string',
    'text_len': 'int64'
    })

if __name__ == '__main__':
    df.info()
    print('number of tweets found: {}'.format(tweet_ct))
    print('end')

