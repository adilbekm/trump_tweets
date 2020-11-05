# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from load_tweets import df

total = len(df)
print('found {} total tweets'.format(total))


# 1: number of tweets by year

f_name = 'plt_01.png'

fig = plt.figure() # creates current figure
ax = plt.subplot() # creates current axes

ax.set_title('Number of Tweets by Year')

yrs = ['2017', '2018', '2019', '2020']
ts = []
for yr in yrs:
    count = len(df[df['created_yy'] == int(yr)])
    ts.append(count)

bars = ax.bar(yrs, ts)

# annotate top of each bar with count of tweets for the year that the bar represents
for i, bar in enumerate(bars):
    bar_height = bar.get_height()
    tcount = '{:,}'.format(ts[i])
    ax.annotate(
        tcount,
        xy=(bar.get_x() + bar.get_width() / 2, bar_height),
        xytext=(0, 3),
        textcoords='offset pixels',
        horizontalalignment='center')

# y-axis seems kind of short, so make it 5% taller 
_, _, ymin, ymax = plt.axis()
ax.set(ylim=(ymin, ymax * 1.05)) 

#ax.set_xlabel('Year')
#ax.set_ylabel('Tweets')

fig.savefig('plt_01.png')
plt.close() # closes current figure (not required but keeps the memory clean)

print('created plot {}'.format(f_name))


