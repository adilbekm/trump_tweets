# All the President's Tweets #

![Banner with tweets][plt14]

**President Trump has sent 23,858 tweets since taking office in 2017. I downloaded all of them from Twitter to look for patterns, and here is what I found in a few graphs.** 

Donald Trump had been a prolific tweeter even before he became President, sending thousands of tweets per year. When he was elected in 2016, there was an expectation that he might mold into the job and change some of his habits, including his tweeting habit. But that expectation turned out to be short-lived because not only President Trump continued to tweet on a daily basis, he has increased the number of tweets he sent from one year to the next.

![Tweets by year][plt1]

### Tweets vs. Retweets

If you don't use Twitter very often, it's worth mentioning that tweets can be of two types, own tweets or retweets. An own tweet is when you type something in 140 characters or less and send it out, and a retweet is when you take someone else's tweet and send it out, optionally including your comment in 140 characters. So, here is a look at President Trump's tweets broken into these two types:

![Tweets vs retweets][plt2]

This graph reveals a couple of interesting patterns. First, even with the retweets separated out, President Trump has increased his tweeting frequency with his time in the White House. In other words, his tweeting activity has grown regardless of the type of tweeting. Second, his retweeting rate has increased even more drastically than the rate of his own tweets, bringing the ratio of own tweets to retweets to almost half-and-half by 2020. It is almost like he has realized the value of retweets around the middle of his Presidency, and then turned them into a routine. 

### Tweets by Month

23,858 tweets in the past 4 years and counting certainly feels like a big number, but to better understand what this volume of tweets really means, it is useful to break up the years into months and look at the tweets on a month-by-month basis.

![Tweets per month][plt4]

We now see that in the first two years of his Presidency, the increase in the number of tweets happened at a relatively calm rate, going from 208 tweets per month in 2017 to about 285 tweets per month in 2018. But that changed in a big way from 2019, with his tweeting rate more than doubling to 610 tweets per month in that year, and further increasing to almost a thousand tweets per month in 2020. What happened?

We know that 2019 was the year of his impeachment trial, and 2020 has been dominated by the pandemic, economy, and the elections. But one could argue that Trump's whole time in office was extraordinarily eventful with things like the Mueller investigation, the trade war with China, and foreign policy shifts, so the answer might not be entirely clear.

It is also interesting to see a seasonal pattern in President Trump's tweets. It appears that his tweeting activity subsides in the colder months of the year and picks up in the summer and fall, although this pattern seems to hold better in the early years than later.  

### Tweets vs. Likes

What about Likes? Here is basically the previous graph but superimposed with Likes using a secondary y-axis on the right:

![Tweets per month with likes][plt6]

Despite a roller coaster-like tweeting rate, the Likes remained relatively steady in the range from 50 to 100 thousand Likes per tweet on average. Notice how the red line that represents Likes stays above the volume of tweets in the first two years, but drops below them in the later years. What this likely shows is that more tweeting didn't translate to more Likes per tweet. Actually, if there is any relationship between the volume of tweets and their likeability, it appears to be a negative one where more tweeting is making the tweets less popular. This is more noticeable in 2018 and 2019. 

You can also observe an annual pattern with the Likes where they seem to be higher in the beginning and end of the year, and lower in the middle. Of course, this is not to suggest that the likeability of tweets is driven by natural seasons, but more likely by the content of the tweets which in its own turn might be driven by seasons.

It would be an omission to move on without mentioning the spike in Likes in November of 2020. There are a few reasons that make this month special, but chief among those, of course, is the loss of his re-election. It is possible that the spike is a show of support from his followers on Twitter in light of the hard news, but it would be wrong to put too much weight on the month because this is an incomplete month (the dataset includes tweets up to 9:00 am on November 24, 2020), and because many of Trump's tweets in November were flagged with Twitter's new disinformation label, making them not possible to interact with. And that leaves the month with even fewer tweets to work with for calculating average likes. 

### Tweets by Day of Week

Most people structure their days differently based on the day of the week, and the most common example of that is weekdays versus weekends. We do things differently on our days off versus our work days: we watch TV more or less, exercise more or less, and use social media more or less. Can we observe any such patterns with President Trump's tweets during his week?

![Tweets by day of week][plt7]

It turns out, President Trump tweets remarkably consistently every day of the week. Although there appears to be a small rise and decline as the week unfolds, especially in 2017 and 2018, by and large President Trump does not appear to take any days off from Twitter. In 2020, this slight pattern even reverses, and the middle of the week actually becomes the less active period (although with over 30 tweets per day it is less active only by a few tweets). 

### Tweets by Time of Day

It has been common to hear reports of President Trump sending tweets very late at night or very early in the morning, in addition to the usual hours of the day. So when I started working on this dataset, I was curious to see how President Trump's tweeting frequency would look by time of day. And here is what that looks like:

![Tweets by time of day][plt9]

This graph contains a lot of information, but I thought the most striking observation is how little President Trump sleeps, especially in the last two years. Looking at 2020, his bedtime appears to be from about 1:00 am to 6:00 am, a meager 5 hours. And sleep, or whatever is left of it, seems to be the only thing that stops him from tweeting, because in all the other times of the day he sends anywhere from 1 to 3 tweets per hour. 

The period in the morning from 7:00 am to 11:00 am appears to be the most active time of the day, with over 2 tweets per hour, based on the 2020 tweets. And the most active hour within that period is 8:00 am to 9:00 am, with over 3 tweets in that hour. Interestingly, but probably not surprisingly, the next most active period is late at night, from about 9:00 pm to 1:00 am, with about 2 tweets per hour.

### Most (and Least) Active Days

After seeing the remarkable volume and consistency of tweets, it may be interesting to ask what President Trump's most, and least, active tweeting days were. And how many tweets made them qualify for the top rank. So here are President Trump's top 10 most active tweeting days:

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

### All Tweets Day-by-Day in One Graph

Finally, here is a look at all of President Trump's tweets, day-by-day, in one graph (the x-axis shows week numbers, from 1 to 52):

![All tweets day by day][plt13]

### Data and Methodology

I obtained the data for this publication from the Twitter API, and analyzed using Python and its special data libraries NumPy, Pandas, and Matplotlib. The data and scripts can be found at https://github.com/adilbekm/trump_tweets

### Other Graphs 

![Tweets per day][plt3]

![Tweets per month by tweet vs retweet][plt5]

![Tweets by day of week by tweet vs retweet][plt8]

![Tweets by time of day by tweet vs retweet][plt10]

![Days without any tweets][plt12]

You can view any of the tweets from this this dataset at Twitter.com by replacing the ending of the link shown below with the id of the tweet you are interested in, and opening the link in your browser:

https://twitter.com/realDonaldTrump/status/tweet-id-here

November 24, 2020

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
[plt14]: images/plt_14.png

