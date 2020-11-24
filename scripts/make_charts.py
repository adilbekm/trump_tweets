# Script for analyzing tweets and creating visualizations

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from load_tweets import df


total = len(df)
print('found {} total tweets'.format(total))

# dates of the dataset
dataset_start = datetime.date(2017, 1, 1)
dataset_end = datetime.date(2020, 11, 7)

# texts
main_title = 'President Trump\'s Tweets'
fineprint = 'https://github.com/adilbekm/trump_tweets'

# setup colors
tcolor = (0.11, 0.63, 0.95) # twitter color RGB(29, 161, 242)
my_red = (0.9, 0.17, 0.31, 0.9)

# list of years
yrs_array = df['created_yy'].unique()
yrs = sorted(yrs_array) # [2017, 2018, ...]
yrs = [str(yr) for yr in yrs]

def cnt_days(start, end):
    '''Count and return number of days in a closed period (including ends)
    given by the two dates, start and end.
    '''
    delta = end - start
    return delta.days + 1

def cnt_wdays(start, end):
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

def days_in_month(year, month):
    '''Given the year and month, return number of days in that month.
    '''
    if not isinstance(month, int) or month < 1 or month > 12:
        raise Exception('month must be integer from 1 to 12')
    if month == 12:
        nyear = year + 1
        nmonth = 1
    else:
        nyear = year
        nmonth = month + 1
    start = datetime.date(year, month, 1)
    end = datetime.date(nyear, nmonth, 1)
    delta = end - start
    return delta.days

# precalc number of days; careful with 2020 - should be day of last tweet
days2017 = cnt_days(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
days2018 = cnt_days(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
days2019 = cnt_days(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
days2020 = cnt_days(datetime.date(2020, 1, 1), dataset_end)
days_year = [days2017, days2018, days2019, days2020]

# precalc number of days; careful with 2020 - should be day of last tweet
wdays2017 = cnt_wdays(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
wdays2018 = cnt_wdays(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
wdays2019 = cnt_wdays(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
wdays2020 = cnt_wdays(datetime.date(2020, 1, 1), dataset_end)
wdays_year = [wdays2017, wdays2018, wdays2019, wdays2020]


# --------------------------------------------------------------------------- 
# Number of tweets by year

f_name = 'plt_01.png'

fig = plt.figure() # creates current figure
ax = plt.subplot() # creates current axes

title = main_title
ax.set_title(title)
#ax.set_ylabel('Number of Tweets')

ts = []
for y in yrs:
    cnt = len(df[df['created_yy'] == int(y)])
    ts.append(cnt)

bars = ax.bar(yrs, ts, width=0.6, color=tcolor)

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

# format y-labels with a thousands separator and no decimals
#yticks = ax.get_yticks()
#ax.set_yticks(yticks) # needed for FixedLocator
#yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
#ax.set_yticklabels(yticks)

# turn off y-axis
ax.get_yaxis().set_visible(False)

# show y-grid line
#ax.grid(axis='y', which='major', linestyle='--')

# disable spines (axis lines)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Number of tweets by re-tweet vs tweet

f_name = 'plt_02.png'

fig = plt.figure() # creates current figure
ax = plt.subplot() # creates current axes

title = main_title
ax.set_title(title)
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

bars = ax.bar(yrs_tweet, height=ts_tweet, width=0.4, label='Own tweets', color=tcolor)
bars = ax.bar(yrs_retwt, height=ts_retwt, width=0.4, label='Retweets')

# set x-labels to years
ax.set_xticks(np.arange(len(yrs)))
ax.set_xticklabels(yrs)

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
ax.set_yticklabels(yticks)

# show y-grid line
#ax.grid(axis='y', which='major', linestyle='--')

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(frameon=False)

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Average tweets per day

f_name = 'plt_03.png'

#fig = plt.figure(figsize=(13, 5), tight_layout={'rect': (0, 0.02, 1, 1)})
fig = plt.figure(figsize=(13, 5), tight_layout=True)
ax = plt.subplot()

title = main_title
ax.set_title(title)

tyears = []
tmonths = []
for i, y in enumerate(yrs):
    y = int(y)
    for m in range(1, 13):
        tcount = len(df[(df.created_yy == y) & (df.created_mm == m)])
        days = days_in_month(y, m)
        t = tcount / days
        tmonths.append(t)
    tyear = len(df[df.created_yy == y])
    t = tyear / days_year[i]
    tyears.append(t)

#print(tyrs)
#print(tmonths)

ms = len(yrs) * ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'] 
ms_array = np.arange(len(ms))
label = 'Tweets per day (average over month)'
ax.bar(ms_array, height=tmonths, width=0.6, color=tcolor, label=label) 

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
label = 'Tweets per day (average over year)'
ax.hlines(tyears, xmin, xmax, color=my_red, label=label)

# annotate horizontal lines (with the counts)
for i, t in enumerate(tyears):
    x = i * 12 + 0.5
    y = t + 0.5 
    ax.annotate('{:.1f}'.format(t), xy=(x, y), color=my_red, fontweight='bold')

# add years below x-axis, i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-5, s=y, horizontalalignment='center')

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(frameon=False, loc=2, bbox_to_anchor=(0, 1.02))

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Average tweets per month

f_name = 'plt_04.png'

#fig = plt.figure(figsize=(13, 5), tight_layout={'rect': (0, 0.02, 1, 1)}) # creates current figure
fig = plt.figure(figsize=(13, 5), tight_layout=True) # creates current figure
ax = plt.subplot() # creates current axes

title = main_title
ax.set_title(title)
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
label = 'Tweets per month'
ax.bar(ms_array, height=ts, width=0.6, color=tcolor, label=label) 

# set x-labels to months
ax.set_xticks(ms_array)
ax.set_xticklabels(ms)

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
#yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
#ax.set_yticklabels(yticks)

# show y-grid line
ax.grid(axis='y', which='major', linestyle='--')

# add vertical lines to separate years
xloc = [((n * 12) - 0.5) for n in range(1, len(yrs))]
for n in xloc:
    ax.axvline(x=n, ymin=0, ymax=1, linestyle='--', color=(0.1, 0.2, 0.5, 0.5))

# add horizontal lines for monthly averages
xmin = np.array([ 0, 12, 24, 36]) - 0.3 # starting points (adjusted by -0.3)
xmax = np.array([11, 23, 35, 46]) + 0.3 # ending points (adjusted by + 0.3)
label = 'Tweets per month (average over year)'
ax.hlines(ts_avgs, xmin, xmax, color=my_red, label=label)

# annotate horizontal lines (with the counts)
for i, t in enumerate(ts_avgs):
    x = i * 12 + 0.5
    y = t + 15
    ax.annotate('{:.1f}'.format(t), xy=(x, y), color=my_red, fontweight='bold')

# add years below x-axis, i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-150, s=y, horizontalalignment='center')

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# ymax defaults at 1399.65; if so, set it to 1400 even
_, ymax = ax.get_ylim()
if ymax < 1400:
    ax.set_ylim(ymax = 1400)

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(frameon=False)

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Average tweets per month, tweets vs retweets

f_name = 'plt_05.png'

#fig = plt.figure(figsize=(13, 5), tight_layout={'rect': (0, 0.02, 1, 1)}) # creates current figure
fig = plt.figure(figsize=(13, 5), tight_layout=True) # creates current figure
ax = plt.subplot() # creates current axes

title = main_title
ax.set_title(title)
#ax.set_ylabel('Number of Tweets')

rs = []
ts = []
ts_avgs = []
for y in yrs:
    if y == '2020':
        ts_avg = len(df[df.created_yy == int(y)]) / 11
    else:
        ts_avg = len(df[df.created_yy == int(y)]) / 12
    ts_avgs.append(ts_avg)
    for m in range(1, 13):
        subdf = df[(df.created_yy == int(y)) & (df.created_mm == m)]
        cnt_r = len(subdf[subdf.is_retweet == True])
        cnt_t = len(subdf[subdf.is_retweet == False])
        rs.append(cnt_r)
        ts.append(cnt_t)

ms = len(yrs) * ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'] 
ms_array = np.arange(len(ms))
label1 = 'Retweets'
label2 = 'Own tweets'
ax.bar(ms_array, height=rs, width=0.6, label=label1)
ax.bar(ms_array, height=ts, bottom=rs, width=0.6, color=tcolor, label=label2) 

# set x-labels to months
ax.set_xticks(ms_array)
ax.set_xticklabels(ms)

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
#yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
#ax.set_yticklabels(yticks)

# show y-grid line
ax.grid(axis='y', which='major', linestyle='--')

# add vertical lines to separate years
xloc = [((n * 12) - 0.5) for n in range(1, len(yrs))]
for n in xloc:
    ax.axvline(x=n, ymin=0, ymax=1, linestyle='--', color=(0.1, 0.2, 0.5, 0.5))

# add horizontal lines for monthly averages
xmin = np.array([ 0, 12, 24, 36]) - 0.3 # starting points (adjusted by -0.3)
xmax = np.array([11, 23, 35, 46]) + 0.3 # ending points (adjusted by + 0.3)
label = 'Tweets per month (average over year)'
ax.hlines(ts_avgs, xmin, xmax, color=my_red, label=label)

# annotate horizontal lines (with the counts)
for i, t in enumerate(ts_avgs):
    x = i * 12 + 0.5
    y = t + 15
    ax.annotate('{:.1f}'.format(t), xy=(x, y), color=my_red, fontweight='bold')

# add years below x-axis, i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-150, s=y, horizontalalignment='center')

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# ymax defaults at 1399.65; if so, set it to 1400 even
_, ymax = ax.get_ylim()
if ymax < 1400:
    ax.set_ylim(ymax = 1400)

# disable spines (lines across axis)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend()

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Average tweets per month with likes 

f_name = 'plt_06.png'

#fig = plt.figure(figsize=(13, 5), tight_layout={'rect': (0, 0.02, 1, 1)})
fig = plt.figure(figsize=(13, 5), tight_layout=True)
ax = plt.subplot() # first axes for tweets
ax2 = ax.twinx() # second axes for like (sharing the same y-axis)

title = main_title
ax.set_title(title)

ax.set_ylabel('Tweets')
ax2.set_ylabel('Likes', color=my_red)

ts = []
likes = []
for y in yrs:
    y = int(y)
    for m in range(1, 13):
        # get tweets
        cnt = len(df[(df.created_yy == y) & (df.created_mm == m)])
        ts.append(cnt)
        # get likes
        ts2 = len(df[(df.created_yy == y) & (df.created_mm == m) & (df.like_ct > 0)])
        ls = df[(df.created_yy == y) & (df.created_mm == m) & (df.like_ct > 0)].like_ct.sum()
        if ts2 == 0:
            avg_like = np.nan 
        else:
            avg_like = ls / ts2
        likes.append(avg_like)

# set November 2020 likes to np.nan (incomplete month)
#likes[-2] = np.nan

label1 = 'Tweets per month'
ax.bar(ms_array, height=ts, width=0.6, color=tcolor, label=label1)
label2 = 'Likes per tweet (average over month)'
ax2.plot(ms_array, likes, linewidth=2, color=my_red, marker='o', label=label2)

# set x-labels to months
ax.set_xticks(ms_array)
ax.set_xticklabels(ms)

# x-axis limits by default are wasteful, so set my own
xmin = -1
xmax = len(ms)
ax.set(xlim=(xmin, xmax)) 

# add vertical lines to separate years
xloc = [((n * 12) - 0.5) for n in range(1, len(yrs))]
for n in xloc:
    ax.axvline(x=n, ymin=0, ymax=1, linestyle='--', color=(0.1, 0.2, 0.5, 0.5))

# add years below x-axis, i.e. below months
for i, y in enumerate(yrs):
    ax.text(x=(i * 12 + 5.5), y=-150, s=y, horizontalalignment='center')

# format y-labels with a thousands separator and no decimals
yticks = ax.get_yticks()
ax.set_yticks(yticks) # needed for FixedLocator
#yticks = ['{:,.0f}'.format(t) for t in yticks.tolist()]
#ax.set_yticklabels(yticks, color=tcolor)

# set and format secondary y-labels manually, with K for thousands
#yticks = [20000, 40000, 60000, 80000, 100000, 120000]
yticks = [50000, 100000, 150000, 200000]
ax2.set_yticks(yticks)
yticks = ['{:.0f}K'.format(t / 1000) for t in yticks]
ax2.set_yticklabels(yticks, color=my_red)

# y-axis min limits is not zero, so set to zero
ax2.set_ylim(ymin=0)

# disable top spine (lines across x-axis)
ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.legend(frameon=False, bbox_to_anchor=(0, 0.95), loc=2)
ax2.legend(frameon=False)

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Tweets by day of the week

#title = 'Tweets by Day of Week'
f_name = 'plt_07.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout={'rect': (0, 0.02, 1, 1)}) 
ax2017 = plt.subplot(2, 2, 1)
ax2018 = plt.subplot(2, 2, 2)
ax2019 = plt.subplot(2, 2, 3)
ax2020 = plt.subplot(2, 2, 4)
axs = [ax2017, ax2018, ax2019, ax2020]

title = main_title
fig.suptitle(title)

# in python, weekdays are 0 for Mon and 6 for Sun
wkds = [0, 1, 2, 3, 4, 5, 6] # Sun to Sat
ts = []
for i, y in enumerate(yrs):
    t = []
    for d in wkds:
        cnt_ts = len(df[(df.created_yy == int(y)) & (df.created_wd == d)])
        cnt_wd = wdays_year[i][d]
        cnt = cnt_ts / cnt_wd
        t.append(cnt)
    ts.append(t)

for i, ax in enumerate(axs):
    ax.bar(np.arange(7), height=ts[i], color=tcolor)

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

wkds = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    ax.set_xticks(np.arange(len(wkds)))
    ax.set_xticklabels(wkds)
    ax.set_title(yrs[i], y=0.9)
    # set y-ticks manually, default ticks are too granular
    yticks = [10, 20, 30]
    ax.set_yticks(yticks)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', which='major', linestyle='--')

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Tweets by day of the week, tweets vs retweets

f_name = 'plt_08.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout={'rect': (0, 0.02, 1, 1)}) 
ax2017 = plt.subplot(2, 2, 1)
ax2018 = plt.subplot(2, 2, 2)
ax2019 = plt.subplot(2, 2, 3)
ax2020 = plt.subplot(2, 2, 4)
axs = [ax2017, ax2018, ax2019, ax2020]

title = main_title + ': Tweets Per Weekday'
fig.suptitle(title)

# in python, weekdays are 0 for Mon and 6 for Sun
wkds = [0, 1, 2, 3, 4, 5, 6] # Mon to Sun
rs = []
ts = []
for i, y in enumerate(yrs):
    r = []
    t = []
    for d in wkds:
        subdf = df[(df.created_yy == int(y)) & (df.created_wd == d)]
        cnt_rs = len(subdf[subdf.is_retweet == True])
        cnt_ts = len(subdf[subdf.is_retweet == False])
        cnt_wd = wdays_year[i][d]
        cnt_r = cnt_rs / cnt_wd
        cnt_t = cnt_ts / cnt_wd
        r.append(cnt_r)
        t.append(cnt_t)
    rs.append(r)
    ts.append(t)

for i, ax in enumerate(axs):
    ax.bar(np.arange(7), height=rs[i], label='Retweets')
    ax.bar(np.arange(7), height=ts[i], bottom=rs[i], color=tcolor, label='Own tweets')

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

wkds = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    ax.set_xticks(np.arange(len(wkds)))
    ax.set_xticklabels(wkds)
    ax.set_title(yrs[i], y=0.9)
    # set y-ticks manually, default ticks are too granular
    yticks = [10, 20, 30]
    ax.set_yticks(yticks)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', which='major', linestyle='--')

ax2017.legend(frameon=False, loc=2, bbox_to_anchor=(0, 1.02))

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # closes current figure (not required but keeps the memory clean)

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Tweets by time of day

f_name = 'plt_09.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout={'rect': (0, 0.02, 1, 1)})
ax2017 = plt.subplot(2, 2, 1)
ax2018 = plt.subplot(2, 2, 2)
ax2019 = plt.subplot(2, 2, 3)
ax2020 = plt.subplot(2, 2, 4)
axs = [ax2017, ax2018, ax2019, ax2020]

title = main_title + ': Tweets Per Hour'
fig.suptitle(title)

ts = []
hs = list(range(24))
for i, y in enumerate(yrs):
    tweets = [0] * 24
    for h in hs:
        cnt = len(df[(df.created_yy == int(y)) & (df.created_hh == h)])
        cnt_avg = cnt / days_year[i]
        tweets[h] = cnt_avg
    ts.append(tweets)

for i, ax in enumerate(axs):
    ax.bar(hs, height=ts[i], color=tcolor)
    line = ax.axvline(x=12, ymin=0, ymax=0.7, linestyle='--', color=(1.0, 0.65, 0, 0.9))
    ax.text(12, 2.5, 'Noon', color=(1.0, 0.65, 0, 1.0), fontweight='bold', ha='center')

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    #ax.set_title(yrs[i], y=0.90, backgroundcolor='white')
    ax.set_title(yrs[i], y=0.90)
    # set y-ticks manually, default ticks are too granular
    yticks = [1, 2, 3]
    ax.set_yticks(yticks)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', which='major', linestyle='--')

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close()

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Tweets by time of day, tweets vs. retweets

f_name = 'plt_10.png'

fig = plt.figure(figsize=(8.32, 6.24), tight_layout={'rect': (0, 0.02, 1, 1)})
ax2017 = plt.subplot(2, 2, 1)
ax2018 = plt.subplot(2, 2, 2)
ax2019 = plt.subplot(2, 2, 3)
ax2020 = plt.subplot(2, 2, 4)
axs = [ax2017, ax2018, ax2019, ax2020]

title = main_title + ': Tweets Per Hour'
fig.suptitle(title)

rs = []
ts = []
hs = list(range(24))
for i, y in enumerate(yrs):
    r = [0] * 24
    t = [0] * 24
    for h in hs:
        subdf = df[(df.created_yy == int(y)) & (df.created_hh == h)]
        cnt_r = len(subdf[subdf.is_retweet == True])
        cnt_t = len(subdf[subdf.is_retweet == False])
        cnt_r_avg = cnt_r / days_year[i]
        cnt_t_avg = cnt_t / days_year[i]
        r[h] = cnt_r_avg
        t[h] = cnt_t_avg
    rs.append(r)
    ts.append(t)

for i, ax in enumerate(axs):
    ax.bar(hs, height=rs[i], label='Retweets')
    ax.bar(hs, height=ts[i], bottom=rs[i], color=tcolor, label='Own tweets')
    line = ax.axvline(x=12, ymin=0, ymax=0.7, linestyle='--', color=(1.0, 0.65, 0, 0.9))
    ax.text(12, 2.5, 'Noon', color=(1.0, 0.65, 0, 1.0), fontweight='bold', ha='center')

# get largest ymax among all plots
ymaxs = []
for ax in axs:
    _, ymax = ax.get_ylim()
    ymaxs.append(ymax)
ymax = max(ymaxs)

for i, ax in enumerate(axs):
    ax.set_ylim(ymax=ymax)
    #ax.set_title(yrs[i], y=0.90, backgroundcolor='white')
    ax.set_title(yrs[i], y=0.90)
    # set y-ticks manually, default ticks are too granular
    yticks = [1, 2, 3]
    ax.set_yticks(yticks)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', which='major', linestyle='--')

#ax2017.legend(frameon=False, loc=2, bbox_to_anchor=(0, 0.95))
ax2017.legend(loc=2)

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close()

print('saved plot {}'.format(f_name))


# ---------------------------------------------------------------------------
# Most active days

f_name = 'plt_11.png'

fig = plt.figure(figsize=(11, 4), tight_layout={'rect': (0, 0.02, 1, 1.02)})
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

fig.suptitle('Top 10 Most Active Days')
ax1.set_title('By Total Tweets', loc='left')
ax2.set_title('By Own Tweets', loc='left')

zeros = [] # this will be used in next plot, inactive days
top_all = []
top_own = []
days = (dataset_end - dataset_start).days + 1

for n in range(days):
    dd = dataset_start + datetime.timedelta(days=n)
    y = dd.year
    m = dd.month
    d = dd.day
    subdf = df[(df.created_yy == y) & (df.created_mm == m) & (df.created_dd == d)]
    t_all = len(subdf)
    t_own = len(subdf[subdf.is_retweet == False])
    t_ret = len(subdf[subdf.is_retweet == True])
    if t_all == 0:
        zeros.append(dd)
    else:    
        top_all.append((t_all, t_own, t_ret, dd))
        top_all = sorted(top_all, reverse=True)[:10]
        top_own.append((t_own, t_ret, dd))
        top_own = sorted(top_own, reverse=True)[:10]

top_all = top_all[::-1]
top_own = top_own[::-1]

ten = np.arange(10)

a = [a for (a, t, r, d) in top_all]
r = [r for (a, t, r, d) in top_all]
t = [t for (a, t, r, d) in top_all]
d = ['{:%b %d, %Y}'.format(d) for (a, t, r, d) in top_all]

ax1.barh(ten, t, color=tcolor)
ax1.barh(ten, r, left=t)
ax1.set_yticks(ten)
ax1.set_yticklabels(d, fontfamily='monospace')

r2 = [r for (t, r, d) in top_own]
t2 = [t for (t, r, d) in top_own]
d2 = ['{:%b %d, %Y}'.format(d) for (t, r, d) in top_own]
t2offset = [n + 17 for n in t2]

ax2.barh(ten, t2, color=tcolor, label='Own tweets')
ax2.barh(ten, r2, left=t2offset, label='Retweets')
ax2.set_yticks(ten)
ax2.set_yticklabels(d2, fontfamily='monospace')

# show tweet counts
for i in ten:
    ax1.text(t[i] / 2, i, str(t[i]), ha='center', va='center', color='white')
    ax1.text(t[i] + r[i] / 2, i, str(r[i]), ha='center', va='center', color='white')
    ax1.text(t[i] + r[i] + 1, i, str(a[i]), va='center')
    ax2.text(t2[i] + 1, i, str(t2[i]), va='center')
    ax2.text(t2[i] + r2[i] + 18, i, str(r2[i]), va='center', alpha=0.5)

# normalize xmax on both axes
_, xmax1 = ax1.get_xlim()
_, xmax2 = ax2.get_xlim()
xm = max(xmax1, xmax2)
ax1.set_xlim(xmax = xm)
ax2.set_xlim(xmax = xm)

# default x-ticks are too granular, so set my own
ticks = [0, 50, 100, 150, 200]
ax1.set_xticks(ticks)
ax1.set_xticklabels(ticks)
ax2.set_xticks(ticks)
ax2.set_xticklabels(ticks)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

fig.legend()

#fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # close current figure - not required but keeps the memory clean

print('saved plot {}'.format(f_name))


# ---------------------------------------------------------------------------
# Inactive days - no tweeting

# Data for this plot ("zeros") is calculated in previous plot

f_name = 'plt_12.png'

fig = plt.figure(figsize=(10, 1.5), tight_layout={'rect': (0, 0.02, 1, 1)})

fig.suptitle('Days Without Any Tweets')

f = 1.15 # factor for spreading out the dates (1 = no spread)
xoffset = f / (len(zeros) + 1)
x = (1 - f) / 2
for i, z in enumerate(zeros):
    d = '{:%b %d, %Y}'.format(z)
    s = str(i + 1) + ') ' + d
    x += xoffset
    fig.text(x, 0.5, s, ha='center')

fig.text(0.99, 0.03, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close() # close current figure - not required but keeps the memory clean

print('saved plot {}'.format(f_name))


# ---------------------------------------------------------------------------
# Heatmap of daily tweets

f_name = 'plt_13.png'

fig = plt.figure(
        figsize=(15, 10), 
        tight_layout={'rect': (0, 0.02, 1, 1), 'h_pad': 0.7})
ax1 = plt.subplot(4, 1, 1)
ax2 = plt.subplot(4, 1, 2)
ax3 = plt.subplot(4, 1, 3)
ax4 = plt.subplot(4, 1, 4)
axs = [ax1, ax2, ax3, ax4]

title = main_title
fig.suptitle(title, fontsize='x-large')

# number of weeks in 2017-2020: 52 + 52 + 52 + 53 = 209
# but will use 52 for all for years so that graphs align
# so go with np.array of shape (208, 7)
# i will use iso calendar, so week begins with monday

weeks = 208
days = 7
t = np.zeros((weeks, days))
# start on 2017-01-02 because 2017-01-01 is week 52 of 2016
c = dataset_start + datetime.timedelta(days=1)

for wk in range(weeks):
    for wd in range(days):
        y = c.year
        m = c.month
        d = c.day
        tc = len(df[(df.created_yy == y) & (df.created_mm == m) & (df.created_dd == d)])
        t[wk][wd] = tc
        c += datetime.timedelta(days=1)

# max value to use in colormap
tmean = t.mean()
tstd = t.std()
tmax = int(tmean + (2 * tstd)) # 2 stds from mean

# split the array by years:
t1 = t[0:52]
t2 = t[52:104]
t3 = t[104:156]
t4 = t[156:]

# trasponse (for imshow)
t1 = np.transpose(t1)
t2 = np.transpose(t2)
t3 = np.transpose(t3)
t4 = np.transpose(t4)

ts = [t1, t2, t3, t4]

for i, ax in enumerate(axs):
    ax.imshow(ts[i], cmap='Reds', vmax=tmax)
    ax.set_yticks(np.arange(7))
    ax.set_yticklabels(['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'])
    ax.set_ylabel(yrs[i], fontsize='large')
    ax.set_xticks([0, 9, 19, 29, 39, 49])
    ax.set_xticklabels([1, 10, 20, 30, 40, 50])
    ax.tick_params(
            axis='x', 
            top=True, 
            bottom=False, 
            labeltop=True, 
            labelbottom=False)

# show tweet counts
for i, ax in enumerate(axs):
    for n in range(7):
        for m in range(52):
            cnt = str(int(ts[i][n][m]))
            ax.text(m, n, cnt, ha='center', va='center', fontsize='small', color='w', alpha=0.8)

fig.text(0.99, 0.01, fineprint, ha='right', fontsize='small', fontstyle='italic', alpha=0.5)

fig.savefig(f_name)
plt.close()

print('saved plot {}'.format(f_name))


# --------------------------------------------------------------------------- 
# Banner image, based on previous plot's data for 2019 (t3)

f_name = 'plt_14.png'

fig = plt.figure(figsize=(35, 5), tight_layout=True)
ax = plt.subplot()

ax.imshow(t3, cmap='Reds', vmax=tmax)
ax.set_axis_off()

# show tweet counts
for n in range(7):
    for m in range(52):
        cnt = str(int(t3[n][m]))
        ax.text(m, n, cnt, ha='center', va='center', fontsize='large', color='w', alpha=0.8)

fig.savefig(f_name)
plt.close()

print('saved plot {}'.format(f_name))

