import tweepy
from tweepy import OAuthHandler


consumer_key = 'YOUR_COSTUMER_KEY'
consumer_secret = 'YOUR_COSTUMER_SECRET_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
access_secret = 'YOUR_ACCESS_SECRET_TOKEN'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
saveFile = open('tweetFile.txt', 'a', encoding='utf-8')


for tweet in tweepy.Cursor(api.search,q="*",geocode="22.216763,-100.968527,50km").items(100):
    #print ([tweet.text.encode('utf-8')])
    saveFile.write("%s\n"%(tweet.text))

