
# Time series forecasting of covid cases and sentiment analysis of tweets on covid.

1. Time series forcast for the number of confirmed cases for India is done using:
    a) LSTM.
    b) SVM-regression
    c) Linear regression
    d) mlp
    e) ARIMA statistical model
    and the comparative performance analysis is done.

Time series data of the confirmed, deaths and recovered cases is <span class="highlighter highlight-on"><span class="highlighter highlight-on"><span class="highlighter highlight-on">collected</span></span></span> from https://pomber.github.io/covid19/timeseries.json and https://github.com/CSSEGISandData/COVID-19

The collected data is visualized using matplolib and plotly for map visualization and the models are developed using scikit-learn and pytorch.

2. Sentiment analysis on the tweets on covid is done.

Tweets are collected using the tweepy API by the twitter developers and GetOldTweets3 package in python.

NTLK library is used for the preprocessing and textblob and NLTK for the sentiment analysis.

**Future scope**

The dataset used doesn't include spatial information. Future work would be location specific forecasting.

**IDEA for future implementation:**

Forecasting the sentiment of the tweets on covid. The idea is to basically combine the time series forecasting and sentiment analysis concepts to learn and predict how the people's sentiment on Covid is changing temporally.
