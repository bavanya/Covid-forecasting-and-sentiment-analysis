import os
import tweepy as tw
import re
from textblob import TextBlob


consumer_key = 'uhSPcyJOGceaZ4lWFHQ39yUc9'
consumer_secret = 'woK4EkMkY25KgsffEZFNwXzQXpXuQEhcx3RWJlLxy9LYmw7E2E'
access_token = '1297933875818057740-OWeuYjt7LLjrbiSr3fElf3K3IPZG3q'
access_token_secret = 'JyouAqjyYHn7w9osSr4wo6Ye9jGgo2U3WSAddsl45xhm8'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#fetching tweets
tweets = tw.Cursor(api.search, q="corona",lang="en",since="2020-01-01").items(200)

#cleaning tweets
def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet): 
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(clean_tweet(tweet)) 
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else: 
        return 'negative'
    
alltweets=[]    #list of all tweets with its sentiment

for tweet in tweets:  
    parsed_tweet = {} 
    parsed_tweet['text'] = tweet.text 
    parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text) 
 
    if tweet.retweet_count > 0: 
    # if tweet has retweets, ensure that it is appended only once 
        if parsed_tweet not in alltweets: 
            alltweets.append(parsed_tweet) 
    else: 
        alltweets.append(parsed_tweet) 

# positive tweets list from alltweets 
ptweets = [tweet for tweet in alltweets if tweet['sentiment'] == 'positive'] 
# percentage of positive tweets 
print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(alltweets))) 
# negative tweets list from alltweets 
ntweets = [tweet for tweet in alltweets if tweet['sentiment'] == 'negative'] 
# percentage of negative tweets 
print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(alltweets))) 
# percentage of neutral tweets 
print("Neutral tweets percentage: {} %".format(100*(len(alltweets) -(len( ntweets )+len( ptweets)))/len(alltweets))) 
