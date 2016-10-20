import tweepy
import unicodedata
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
from guess_language import guess_language
import matplotlib.pyplot as plt
import numpy as np

property_globals = {
    'consumer_key'        : 'K1ZfpAvv2x75NEilFHC4KtQUy',
    'consumer_secret'     : '6JSEK3Yl9NI3IYy7yVG64aDMZguJe39nh90VKQ2Jeq9UXlLY6Y',
    'access_token'        : '786975951724961793-Kwb2PWOOGfJfEShCmT0BNweVU3my27g',
    'access_token_secret' : 'fi8ogWzah6B9ogI2N2swml3WyZDLdZS9d5aV0tmghAyFI'
}

# Stream class for filter and search
class FilterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


auth = tweepy.OAuthHandler(property_globals['consumer_key'], property_globals['consumer_secret']);
auth.set_access_token(property_globals['access_token'], property_globals['access_token_secret']);

api = tweepy.API(auth);

collected_tweets = []
sentimented_tweets = []

search_query = tweepy.Cursor(api.search, q='#selfie').items(150);

for tweet in search_query:
    if(guess_language(tweet.text) == "en"):
        collected_tweets.append(tweet.text)

for tweet in collected_tweets:
    try: 
        print tweet
        vs = vaderSentiment(tweet)
        print "\n\t"+str(vs)
        print "\n\n\n"
        sentimented_tweets.append((tweet, vs))
    except:
        continue

pos_collect  = []
neg_collect  = []
comp_collect = []


for sentiments in sentimented_tweets:
    pos_collect.append(sentiments[1].get("pos"))
    neg_collect.append(sentiments[1].get("neg"))
    comp_collect.append(sentiments[1].get("compound"))

N = range(len(sentimented_tweets))

print "\n\n\n\n",N,"\n\n\n\n"

fig = plt.figure()
ax = fig.add_subplot(111)

pos_bar  = plt.bar(N, pos_collect, 0.5,
                 color='b',
                 yerr=None,
                 alpha=0.5,
                 error_kw=dict(elinewidth=2,ecolor='red'))

neg_bar  = plt.bar(N, neg_collect, 0.5,
                 color='r',
                 yerr=None,
                 alpha=0.5,
                 error_kw=dict(elinewidth=2,ecolor='red'))

comp_bar = plt.bar(N, comp_collect, 0.5,
                 color='g',
                 yerr=None,
                 alpha=0.5,
                 error_kw=dict(elinewidth=2,ecolor='red'))

plt.show()

#plt.plot([sentiments[1].get("pos"), sentiments[1].get("neg"), sentiments[1].get("compound")])
#plt.ylabel("float")
#plt.show()

# google_tweets = tweepy.Cursor(api.search, q='google', count=100).items();

# for tweet in google_tweets:
#     print tweet.text,"\n";

# public_tweets = api.home_timeline();
# for tweets in public_tweets:
#     print tweets.text

### Stream stuff:
#fsl = FilterStreamListener()
#collected_tweets.append(stream.filter(languages = ["en"], track = ['google']))
#stream = tweepy.Stream(auth = api.auth, listener = fsl)
