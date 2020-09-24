
#Time series forecasting of covid cases and sentiment analysis of tweets on covid

1. Time series forcast for the number of confirmed cases for India is done using LSTM.

Time series data of the confirmed, deaths and recovered cases is collected from https://pomber.github.io/covid19/timeseries.json and https://github.com/CSSEGISandData/COVID-19

The collected data is visualized using matplolib and plotly.

2. Sentiment analysis on the tweets on covid is done.

Tweets are collected using the tweepy API by the twitter developers and GetOldTweets3 package in python.

NTLK library is used for the preprocessing and textblob and NLTK for the sentiment analysis
