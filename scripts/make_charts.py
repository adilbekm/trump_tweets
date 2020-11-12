# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from load_tweets import df


total = len(df)
print('found {} total tweets'.format(total))


# list of years
yrs_array = df['created_yy'].unique()
yrs = sorted(yrs_array) # [2017, 2018, ...]
yrs = [str(yr) for yr in yrs]

title = 'President Trump\'s Tweets\n'

def cnt_wkdays(start, end):
    '''Count number of weekdays in a period given by two dates, start and end,
    where both dates are inclusive. Return results as a list of 7 numbers,
    Monday through Sunday, where each number is the count of that weekday.
    '''
    res = [0, 0, 0, 0, 0, 0, 0]
    delta = end - start
    days = delta.days
    for i in range(days + 1):
        cur = start + datetime.timedelta(days=i)
        wday = cur.weekday()
        res[wday] = res[wday] + 1
    return res



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



# 4: number of tweets by day of the week

#title = 'Tweets by Day of Week'
f_name = 'plt_04.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout=True) 
ax_2017 = plt.subplot(2, 2, 1)
ax_2018 = plt.subplot(2, 2, 2)
ax_2019 = plt.subplot(2, 2, 3)
ax_2020 = plt.subplot(2, 2, 4)
axs = [ax_2017, ax_2018, ax_2019, ax_2020]

# pre-calc number of weekdays
# be careful with last day of 2020: should be day of last tweet
wkdays2017 = cnt_wkdays(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
wkdays2018 = cnt_wkdays(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
wkdays2019 = cnt_wkdays(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
wkdays2020 = cnt_wkdays(datetime.date(2020, 1, 1), datetime.date(2020, 11, 7))
wkdays = [wkdays2017, wkdays2018, wkdays2019, wkdays2020]

# in python, wkdays are 0 for Mon and 6 for Sun
wkds = [6, 0, 1, 2, 3, 4, 5] # Sun to Sat
ts = {}
for i, y in enumerate(yrs):
    t = []
    for d in wkds:
        cnt_ts = len(df[(df.created_yy == int(y)) & (df.created_wd == d)])
        cnt_wd = wkdays[i][d]
        cnt = cnt_ts / cnt_wd
        t.append(cnt)
    ts[int(y)] = t

for i, ax in enumerate(axs):
    ax.bar(np.arange(7), height=ts[int(yrs[i])])

# get largest ymax across all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
max_ymax = max(ymaxs)

wkds = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for i, ax in enumerate(axs):
    ax.set_ylim(ymax = max_ymax)
    ax.grid(axis='y', which='major', linestyle='--')
    ax.set_xticks(np.arange(len(wkds)))
    ax.set_xticklabels(wkds)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(yrs[i], y=0.95)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


