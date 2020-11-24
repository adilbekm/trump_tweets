# All the President's Tweets #

November 22, 2020

President Trump has sent 23,842 tweets since taking office in 2017. I downloaded all them from Twitter to analyze his tweeting patterns, and here is what I found in a few graphs. 

Donald Trump had been a prolific tweeter even before he became President, sending thousands of tweets per year. When he was elected in 2016, there was an expectation that he might mold into the job and change some of his habits, including his tweeting habit. But that expectation turned out to be short-lived because not only President Trump continued to tweet on a daily basis, he has increased the number of tweets he sent from one year to the next:

![Tweets by year][plt1]

If you don't use Twitter very often, it's worth mentioning that tweets can be of two types - own tweets or retweets. An own tweet is when you type something in 140 characters or less and send it out, and a retweet is when you take someone else's tweet and send it out, optionally including your comment in 140 characters. So, here is a look at President Trump's tweets broken down by these two types: 

![Tweets vs retweets][plt2]

This graph reveals a couple of interesting patterns. First, even with the retweets separated out, President Trump has still increased his tweeting frequency with his time in the White House. In other words, his tweeting activity has grown regardless of the type of tweeting. Second, his retweeting rate has increased even more drastically than the rate of his own tweets, bringing the ratio of own tweets to retweets to almost half-and-half by 2020. It is almost like he has realized the value of retweets around the middle of his Presidency, and then turned them into a routine. 

## Tweets by Month

23,842 tweets over the past 4 years and counting certainly feels like a big number, but to better understand what this volume of tweets really means, it is useful to break up the year into months and look at the tweets on a month-by-month basis:

![Tweets per month][plt4]

We now see that in the first two years of his Presidency, the increase in the number of tweets happened at a relatively calm rate, going from 208 tweets per month in 2017 to about 285 tweets per month in 2018. But changed in a big way from 2019 with his tweeting rate inceasing to 610 tweets per month in that year, and further increasing to almost a thousand tweets per month in 2020. What happened? We know that 2019 was the year of his impeachment trial and 2020 has been dominated by the pandemic, economy, and the elections, but one could argue that Trump's entire term was extraordinarily eventful with things like the Mueller investigation, the trade war with China, and foreign policy shifts, so it is not entirely clear.

It is also interesting to see a seasonal pattern in President Trump's tweets. It appears that his tweeting activity subsides in the colder months of the year and picks up in the summer and fall, although this pattern is more clear in the early years than the later.  

## Tweets and Likes

What about likes? Here is basically the previous graph but overlayed with likes using a secondary y-axis on the right:

![Tweets per month with likes][plt6]

Despite a roller coaster-like tweeting rate, the likes remained relatively steady in the range from 50 to 100 thousand likes per tweet on average. Notice how the red line representing likes stays above the tweets in the first two years, but after that, the likes are below the tweets. More tweeting doesn't appear to have translated to more likes per tweets.

You can also observe an annual pattern with the likes where they seem to be higher in the beginnings and ends of the year, and lower in the middle. This is not to suggest that the likeability of tweets is driven by natural seasons, but more likely by the content of the tweets, which might be varying with the seasons. If there is any relationship between the volume of tweets and their likeability, it appears to be a negative one - more tweeting appears to make the tweets less popular. This is more noticable in 2018 and 2019. 

It would be an omission to move on without mentioning the spike in likes in November of 2020. There are a few reasons that make this month special, but chief among those is, of course, the defeat in the election. It is possible that the spike is a show of support from his followers on Twitter. However, it is hard to put too much weight to November because this is an incomplete month (the dataset includes tweets up to November 22), and because many of Trump's tweets in November were flagged with Twitter's new disinformation label, making them not possible to interact with, leaving even fewer tweets to work with for calculating average likes. 

## Tweets by Day of Week

Most people structure their days differently based on the day of the week, with the most common example of that being weekdays versus weekends. Do President Trump tweets show any such pattern during the 7-day week?

![Tweets by day of week][plt7]

It turns out, President Trump tweets remarkably consistently every day of the week. Although we see a small rise and decline as the week progresses, as visible in 2017 and 2018, by and large President Trump does not appear to take any days off from Twitter. In 2020, the pattern even reverses as the middle of the week becomes the least active period of the week, although with over 30 tweets per day it is difficult to call the period least active. 

## Tweets by Time of Day

It has become common to hear reports of President Trump sending tweets very late at night or very early in the morning, all in addition to the usual hours of the day. So when I started working on this dataset I was curious to see how President Trump's tweeting frequency would look by time of day, and here is what that looks like:

![Tweets by time of day][plt9]

This graph contains a lot of information, but I thought the most striking observation might be how little President Trump sleeps, especiallhy in the last two years. Looking at 2020, his bedtime appears to be from about 1:00am to 6:00am, a meager 5 hours. And sleep, or whatever is left of it, seems to be the only thing that stops him from tweeting because in all other times of the day he sends anywhere from 1 to 3 tweets per hour. 

The period of the morning hours from 7:00am to 11:00am appears to be the most active time of the day, with 2 or more tweets per hour, based on the 2020 tweets. And the most active hour within that period is 8:00am to 9:00am, with over 3 tweets per hour. Interestingly, but probably not surprisingly, the next most active period is the late night from about 9:00pm to 1:00am. 

## Most and Least Active Days

After seeing the remarkable volume and consistency of tweets, it may be interesting to ask what President Trump's most (and least) active tweeting days were, and how many tweets made them qualify for the top rank. So here are President Trump's top 10 most active tweeting days:

![Top 10 most active days][plt11]

With 193 tweets sent in a single day, Friday, June 5, 2020 is the winner. And excluding retweets, Monday, November 2, 2020 is the winner with 70 tweets (and 10 retweets) in a day. 

We can also flip the charts and look at the least active days, or days without any tweeting. It turns out, during his entire Presidency, Donald Trump had only 7 days when he didn't tweet:

1) Saturday, April 15, 2017
2) Thursday, June 8, 2017
3) Friday, October 6, 2017
4) Wednesday, January 31, 2018
5) Monday, February 26, 2018
6) Sunday, May 6, 2018
7) Saturday, March 23, 2019

## All Tweets Day by Day in One Graph

And finally, a look at all of President Trump's tweets, day-by-day, in one graph:

![All tweets day by day][plt13]

## Data and Methodology

I obtained the data from Twitter's API and analyzed it using Python and its data analysis libraries NumPy, Pandas, and Matplotlib. All data and scripts used for this article can be found at: https://github.com/adilbekm/trump_tweets


## Other Graphs 

![Tweets per day][plt3]

![Tweets per month by tweet vs retweet][plt5]

![Tweets by day of week by tweet vs retweet][plt8]

![Tweets by time of day by tweet vs retweet][plt10]

![Days without any tweets][plt12]


You can view any of the tweets from this this dataset at Twitter.com by replacing the ending of the link shown below with the id of the tweet you are interested in, and opening the link in your browser:

https://twitter.com/realDonaldTrump/status/tweet-id-here



## Trash


Yes, there is some increase on work days compared to weekends, but by and large the volume of tweet is

At least in the first two years of his term, there appears to be some structure with a slight reduction in tweets on Sundays and equally limited rise during the week, 


their days differently during the week, with the most common weekends are different from weekdays in what we do and how much, and there are days of the week when we exercise Your weekend may not be the typical Saturday and Sunday, but And there are days when for President Trump's tweeting they are nearly the same.
 
Has President Trump tweeted differently based on the day of the week? It turns out, Trump's tweeting volume does not fluctuate much throughout a whole week. 

The impeachment trial took place in the second half of 2019, and 2020 was dominated by the global pandemic and the elections.  

 We still see that President Trump has sent an increasing number of tweets while in Office, but now we also see that the increase wasn't linear. There is a relatively calm first half of his term followed by a rapidly increasing second half, which can likely be attributed to his impeachment trial in 2019, and of course, the global pandemic and the elections in 2020. Clearly, President Trump 


I next looked at the tweets

 exactly does it mean? How many tweets does this translate to on a monthly basis?  sounds like a big number, 




Interpreting growith in retweets:

Given that retweeting involves 

retweeting:
- read others
- give voice to others
- spread something
- pick and choose
- engagement


What is interesting here is President Trump 


>>>

How can we interprete this second pattern?

Retweeting is a sign of engaging with other users on Twitter, as in connecting with others and sharing their message. So when we see the share of retweets go from sigle digits in the first years to nearly half of all his tweets by now, it may show   

so increased retweeting is a sign of increased engagement with others. So when we see the share of retweets go from single digits in the beginning of his term to almost 50% of his tweets by 2020, it shows that President Trump is finding more connections and support. And a President being no ordinary user, these connections are also likely among organizations or high-profile individuals. 
is of course no ordinary user, the users he interacts with are also not ordinary people, so the connections that the retweets show are likely  

 and this is what we see in the case of President Trump's increased retweeting too.

 President, of course, is no ordinary user, and the users that he interacts with are not ordinary people either.  so this is     these are usually organizations or other high-profile individuals.

>>>

 

sand more.oending more and more tweets the longer he was at the White House. 

has tweeted increasingly more the longer sent increasingly more tweets the longer he was at the White House. 

He continued to tweet daily after moving into the White House, and the longer he stayed there the more he tweeted. 


 become at least a little like all the other presidents that came before him, and this meant tweeting less. But today with nearly all of his presidency behind him, that expectation turned out to be short-lived. 

sending multiple tweets every day. If there was any expectation that this habit would stop after his election, it turned out to be short-lived. He continued to tweet nearly as usual in the first half of his term, and then 



and that included dialing down on his twitting habits. After all, there are many established ways for a President to communicate to the world. Twitter just didn't seem like the best tool for the new job.
 
  When and after he was elected, I expected that he would 

President Trump has sent a total of 23,384 tweets between January 1, 2017 and November 7, 2020 at noon. 

Since becoming President in 2017, Donald Trump has sent 23,787 tweets. To understand this number, I downloaded the tweets and put them into charts.

One of the most unusual things about President Trump is how much he tweets.

I downloaded all of President Trump's tweets since he became President in 2017 to understand his tweeting habits. Here is what I found. 

This is a lot for anyone, so to understand how and To understand what this number means, and his tweeting habit, I downloaded all of his tweets and analyzed them in a few graphs, and here is what I found.

President Trump tweets a lot. But how much exactly does he tweet? How many tweets does he send in a given year, month, day, or even an hour? How many likes does he get? In this article I pulled all of President Trump's tweets since 2017 to answer these questions. 




Last updated: November 20, 2020

[plt1]: images/plt_01.png
[plt2]: images/plt_02.png
[plt3]: images/plt_03.png
[plt4]: images/plt_04.png
[plt5]: images/plt_05.png
[plt6]: images/plt_06.png
[plt7]: images/plt_07.png
[plt8]: images/plt_08.png
[plt9]: images/plt_09.png
[plt10]: images/plt_10.png
[plt11]: images/plt_11.png
[plt12]: images/plt_12.png
[plt13]: images/plt_13.png

