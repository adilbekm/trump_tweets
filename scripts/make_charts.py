# Script for analyzing tweets and creating visualizations

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from load_tweets import df


total = len(df)
print('found {} total tweets'.format(total))


# twitter color (29, 161, 242) (0.11, 0.63, 0.95)
tcolor = (0.11, 0.63, 0.95)

# list of years
yrs_array = df['created_yy'].unique()
yrs = sorted(yrs_array) # [2017, 2018, ...]
yrs = [str(yr) for yr in yrs]

title = 'President Trump\'s Tweets\n'

def cnt_days(start, end):
    '''Count and return number of days in a closed period (including ends)
    given by the two dates, start and end.
    '''
    delta = end - start
    return delta.days

def cnt_wkdays(start, end):
    '''Count and return number of weekdays in a closed period (including ends)
    given by the two dates, start and end. Return results as a list of 7 numbers,
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

bars = ax.bar(yrs, ts, color=tcolor)

# annotate top of each bar with count of tweets for the year that the bar represents
for i, bar in enumerate(bars):
    bar_height = bar.get_height()
    tcount = '{:,}'.format(ts[i])
    ax.annotate(
        tcount,
        xy=(bar.get_x() + bar.get_width() / 2, bar_height),
        xytext=(0, 5),
        textcoords='offset pixels',
        horizontalalignment='center',
        fontsize='large',
        fontweight='bold',
        color=tcolor)

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

bars = ax.bar(yrs_tweet, height=ts_tweet, width=0.4, label='tweet', color=tcolor)
bars = ax.bar(yrs_retwt, height=ts_retwt, width=0.4, label='retweet')

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

ax.legend()

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
ts_avgs = []
for y in yrs:
    if y == '2020':
        ts_avg = len(df[df.created_yy == int(y)]) / 11
    else:
        ts_avg = len(df[df.created_yy == int(y)]) / 12
    ts_avgs.append(ts_avg)
    for m in range(1, 13):
        cnt = len(df[(df.created_yy == int(y)) & (df.created_mm == m)])
        ts.append(cnt)

ms = len(yrs) * ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'] 
ms_array = np.arange(len(ms))
ax.bar(ms_array, height=ts, width=0.6, color=tcolor) 

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

# add horizontal lines for monthly averages
xmin = np.array([ 0, 12, 24, 36]) - 0.3 # starting points (adjusted by -0.3)
xmax = np.array([11, 23, 35, 46]) + 0.3 # ending points (adjusted by + 0.3)
label = 'Average tweets per month'
my_red = (0.9, 0.17, 0.31, 0.9)
ax.hlines(ts_avgs, xmin, xmax, color=my_red, label=label)

# annotate horizontal lines (with the counts)
for i, t in enumerate(ts_avgs):
    x = i * 12 + 1
    y = t + 10
    ax.annotate('{:.1f}'.format(t), xy=(x, y), color=my_red, fontweight='bold')

# add years below x-axis, i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-150, s=y, horizontalalignment='center')

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()

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
    ax.bar(np.arange(7), height=ts[int(yrs[i])], color=tcolor)

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

wkds = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    #ax.grid(axis='y', which='major', linestyle='--')
    ax.set_xticks(np.arange(len(wkds)))
    ax.set_xticklabels(wkds)
    ax.set_title(yrs[i], y=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))



# 5: number of tweets by time of day

#title = 'Tweets by Time of Day'
f_name = 'plt_05.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout=True)
#ax = plt.subplot()
ax2017 = plt.subplot(2, 2, 1)
ax2018 = plt.subplot(2, 2, 2)
ax2019 = plt.subplot(2, 2, 3)
ax2020 = plt.subplot(2, 2, 4)
axs = [ax2017, ax2018, ax2019, ax2020]

# precalc number of days
# be careful with last day of 2020: should be day of last tweet
days2017 = cnt_days(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
days2018 = cnt_days(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
days2019 = cnt_days(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
days2020 = cnt_days(datetime.date(2020, 1, 1), datetime.date(2020, 11, 7))
days = [days2017, days2018, days2019, days2020]

ts = []
hs = list(range(24))
for i, y in enumerate(yrs):
    tweets = [0] * 24
    for h in hs:
        cnt = len(df[(df.created_yy == int(y)) & (df.created_hh == h)])
        cnt_avg = cnt / days[i]
        tweets[h] = cnt_avg
    ts.append(tweets)

for i, ax in enumerate(axs):
    ax.bar(hs, height=ts[i], color=tcolor)
    line = ax.axvline(x=12, ymin=0, ymax=0.7, linestyle='--', color=(1.0, 0.65, 0, 0.9))
    ax.text(12, 2.25, 'Noon', color=(1.0, 0.65, 0, 1.0), fontweight='bold', ha='center')
    #ax.minorticks_on()

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    ax.set_title(yrs[i], y=0.90)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

fig.savefig(f_name)
plt.close()

print('saved plot {}'.format(f_name))



# 6: Average tweets per day, by month and year

#title = 'Average Tweets per Day'
f_name = 'plt_06.png'

fig = plt.figure() # need figsize and tight_layout later
ax = plt.subplot()


