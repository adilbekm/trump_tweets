# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from load_tweets import df


# 1: number of tweets by year

yrs = ['2017', '2018', '2019', '2020']
ts = []
for yr in yrs:
    count = len(df[df['created_yy'] == int(yr)])
    ts.append(count)

fig, ax = plt.subplots()
ax.bar(yrs, ts)

ax.set_title('Number of Tweets by Year')
#ax.set_xlabel('Year')
#ax.set_ylabel('Tweets')

fig.savefig('plt_01.png')



