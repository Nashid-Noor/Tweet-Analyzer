import tweepy
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

analyser = SentimentIntensityAnalyzer()
# The key's to the below 4 lines , Should be generator via your own twitter account.
consumer_key = ''                       
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def sentiment_analyzer_scores(text,engl=True):
    if engl:
        trans = text
    else:
        trans = translator.translate(text).text
    score = analyser.polarity_scores(trans)    
    lb = score['compound']
    if lb >= 0.05:
        return 1
    elif (lb > -0.05) and (lb < 0.05):
        return 0
    else:
        return -1

        

def list_tweets(user_id, count, prt=True):
    tweets = api.user_timeline("@" + user_id, count=count, tweet_mode='extended')
    tw = []
    for t in tweets:
        tw.append(t.full_text)
        if prt:
            print(t.full_text)
           # senti(t.full_text)            
            print()
    return tw


def anl_tweets(lst, title='Tweets Sentiment', engl=True ):
    sents = []
    for tw in lst:
        try:
            st = sentiment_analyzer_scores(tw, engl)
            sents.append(st)
        except:
            sents.append(0)
    ax = sns.distplot(
        sents,
        kde=False,
        bins=3)
    ax.set(xlabel='Negative                Neutral                 Positive',
           ylabel='#Tweets',
          title="Tweets of @"+title)
    return sents

user_id = 'realDonaldTrump' 
count=5
tw_trump = list_tweets(user_id, count)
tw_trump_sent = anl_tweets(tw_trump, user_id)
print(tw_trump_sent)



