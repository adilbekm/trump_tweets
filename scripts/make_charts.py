# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from load_tweets import df

total = len(df)
print('found {} total tweets'.format(total))


# list of years
yrs_array = df['created_yy'].unique()
yrs = sorted(yrs_array) # [2017, 2018, ...]
yrs = [str(yr) for yr in yrs]

title = 'President Trump\'s Tweets\n'



# 1: number of tweets by year

f_name = 'plt_01.png'

fig = plt.figure() # creates current figure
ax = plt.subplot() # creates current axes

#ax.set_title(title)
#ax.set_ylabel('Number of Tweets')

ts = []
for y in yrs:
    cnt = len(df[df['created_yy'] == int(y)])
    ts.append(cnt)

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
#_, _, ymin, ymax = plt.axis()
#ax.set(ylim=(ymin, ymax * 1.05)) 

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for 
yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
ax.set_yticklabels(yticks)

# show y-grid line
ax.grid(axis='y', which='major', linestyle='--')

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))



# 2: number of tweets by re-tweet vs tweet

#title = 'Tweets vs. Retweets'
f_name = 'plt_02.png'

fig = plt.figure() # creates current figure
ax = plt.subplot() # creates current axes

#ax.set_title(title)
#ax.set_ylabel('Number of Tweets')

ts_tweet = []
ts_retwt = []
for y in yrs:
    cnt_tweet = len(df[(df.created_yy == int(y)) & (df.is_retweet == False)])
    cnt_retwt = len(df[(df.created_yy == int(y)) & (df.is_retweet == True)])
    ts_tweet.append(cnt_tweet)
    ts_retwt.append(cnt_retwt)

yrs_tweet = np.arange(len(yrs)) - 0.2
yrs_retwt = np.arange(len(yrs)) + 0.2

bars = ax.bar(yrs_tweet, height=ts_tweet, width=0.4, label='tweet')
bars = ax.bar(yrs_retwt, height=ts_retwt, width=0.4, label='retweet')

# y-axis by default is somewhat short, so make it 5% taller 
#_, _, ymin, ymax = plt.axis()
#ax.set(ylim=(ymin, ymax * 1.05)) 

ax.legend()

# set x-labels to years
ax.set_xticks(np.arange(len(yrs)))
ax.set_xticklabels(yrs)

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
ax.set_yticklabels(yticks)

# show y-grid line
ax.grid(axis='y', which='major', linestyle='--')

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))



# 3: number of tweets by month

#title = 'Tweets by Month'
f_name = 'plt_03.png'

fig = plt.figure(figsize=(12, 5), tight_layout=True) # creates current figure
ax = plt.subplot() # creates current axes

#ax.set_title(title)
#ax.set_ylabel('Number of Tweets')

ts = []
for y in yrs:
    for m in range(1, 13):
        cnt = len(df[(df.created_yy == int(y)) & (df.created_mm == m)])
        ts.append(cnt)

ms = len(yrs) * ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'] 
ms_array = np.arange(len(ms))
ax.bar(ms_array, height=ts, width=0.6) 

# set x-labels to months
ax.set_xticks(ms_array)
ax.set_xticklabels(ms)

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
ax.set_yticklabels(yticks)

# show y-grid line
ax.grid(axis='y', which='major', linestyle='--')

# add vertical lines to separate years
xloc = [((n * 12) - 0.5) for n in range(1, len(yrs))]
for n in xloc:
    ax.axvline(x=n, ymin=0, ymax=1, linestyle='--', color=(0.1, 0.2, 0.5, 0.5))

# add years below x-axis,i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-150, s=y, horizontalalignment='center')

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))



