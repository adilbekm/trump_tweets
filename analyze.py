# Script for analyzing json tweets file and creating graphs


src_filename = 'trump_tweets.json'


import os
import sys
import json
from datetime import datetime, timezone
import numpy as np
import pandas as pd


f_src = open(src_filename, 'r', encoding='utf8')

tweets = json.load(f_src)

total_count = len(tweets)
print('number of tweets found: {}'.format(total_count))


for t in tweets:

    # flatten tweet data
    twt_id = t['id']
    author_id = t['author_id']
    strtime = t['created_et'] # Eastern Time
    created_at = datetime.fromisoformat(strtime) # to str: .isoformat()
    #created_yy = created.year
    #created_mm = created.month
    #created_hh = created.hour
    source = t['source']
    # trump retweets at most 2 tweets, historically
    rt1_id = rt1_type = None
    rt2_id = rt2_type = None
    if 'referenced_tweets' in t:
        rt = t['referenced_tweets']
        rt1_id, rt1_type = rt[0]['id'], rt[0]['type']
        if len(rt) > 1:
            rt2_id, rt2_type = rt[1]['id'], rt[1]['type']
    pm = t['public_metrics']
    pm_rt_ct = pm['retweet_count']
    pm_rp_ct = pm['reply_count']
    pm_lk_ct = pm['like_count']
    pm_qt_ct = pm['quote_count']
    text = t['text'] # need to replace \n?


print('end')



# {'id', 'author_id', 'created_at', 'source', 'public_metrics', 'referenced_tweets', 'entities', 'geo', 'text'}

