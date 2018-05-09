import tweepy
from tweepy import OAuthHandler
from geopy.geocoders import Nominatim



# consumer_key = 'YOUR_COSTUMER_KEY'
# consumer_secret = 'YOUR_COSTUMER_SECRET_KEY'
# access_token = 'YOUR_ACCESS_TOKEN'
# access_secret = 'YOUR_ACCESS_SECRET_TOKEN'
 
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 


class APISearcher(object):

	def Search(self,geoCode,NItems):

		coords = self.GetCoords(geoCode)
		print(coords.latitude,coords.longitude)
		result = ""
		for tweet in tweepy.Cursor(api.search,q="*",geocode=str(coords.latitude)+","+str(coords.longitude)+",50km").items(NItems):
					    result = result + tweet.text + "\n"
					    #saveFile.write("%s\n"%(tweet.text))
					    print(tweet.text.encode("utf-8"))
		return result


	def GetCoords(self,geoCode):
		geolocator = Nominatim()
		location = geolocator.geocode(geoCode)
		return location


 consumer_key = 'YOUR_COSTUMER_KEY'
 consumer_secret = 'YOUR_COSTUMER_SECRET_KEY'
 access_token = 'YOUR_ACCESS_TOKEN'
 access_secret = 'YOUR_ACCESS_SECRET_TOKEN'auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)






