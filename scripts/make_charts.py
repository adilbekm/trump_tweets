# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from load_tweets import df

total = len(df)
print('found {} total tweets'.format(total))


# 1: number of tweets by year

f_name = 'plt_01.png'

fig, ax = plt.subplots()
ax.set_title('Number of Tweets by Year')

yrs = ['2017', '2018', '2019', '2020']
ts = []
for yr in yrs:
    count = len(df[df['created_yy'] == int(yr)])
    ts.append(count)

bars = ax.bar(yrs, ts)

# annotate each bar with the count of tweets at the top of that bar
for i, bar in enumerate(bars):
    bar_height = bar.get_height()
    tcount = '{:,}'.format(ts[i])
    ax.annotate(
        tcount,
        xy=(bar.get_x() + bar.get_width() / 2, bar_height),
        xytext=(0, 3),
        textcoords='offset pixels',
        horizontalalignment='center')

#ax.set_xlabel('Year')
#ax.set_ylabel('Tweets')

fig.savefig('plt_01.png')
print('created plot {}'.format(f_name))


