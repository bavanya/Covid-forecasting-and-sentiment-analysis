import GetOldTweets3 as got
import string
import nltk
nltk.download('vader_lexicon')
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus')\
                                           .setSince("2020-01-01")\
                                           .setUntil("2020-08-31")\
                                           .setLang("en")\
                                            .setNear("India")\
                                           .setTopTweets(200)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets =  get_tweets()
length = len(text_tweets)
print(length)

for i in range(length):
    text = text_tweets[i][0]+" "+text
    print(text)

lower_case=text.lower()
# print(string.punctuation)
clear_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenize_words = word_tokenize(clear_text, "english")
# print(tokenize_words)



final_words = []
for word in tokenize_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# print(final_words)

emotion_list = []

with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        # print("Word : "+ word + " "+ "Emotion : "+ emotion)

        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)

w = Counter(emotion_list)
print(w)

#sentiment_analysis
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos :
        print("Negative Sentiment")
    elif pos > neg :
        print("Positive Sentimnet")
    else:
        print("Neutral Vibe")
    

sentiment_analyse(clear_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

