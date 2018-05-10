import tweepy
import wx
from tweepy import OAuthHandler
from geopy.geocoders import Nominatim
from datetime import datetime
from pytz import timezone
import pytz




# consumer_key = 'YOUR_COSTUMER_KEY'
# consumer_secret = 'YOUR_COSTUMER_SECRET_KEY'
# access_token = 'YOUR_ACCESS_TOKEN'
# access_secret = 'YOUR_ACCESS_SECRET_TOKEN'
 
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 


class APISearcher(object):

	def Search(self,geoCode):

		coords = self.GetCoords(geoCode)
		print(coords.latitude,coords.longitude)
		result = ""
		#Limite 2500 tweets cada 15 min
		if self.checkLimit(): 
			for tweet in tweepy.Cursor(api.search,q="*",geocode=str(coords.latitude)+","+str(coords.longitude)+",80km").items(2500):
						    result = result + tweet.text + "\n"
			return result


	def GetCoords(self,geoCode):
		geolocator = Nominatim()
		try:
			location = geolocator.geocode(geoCode)
			return location
		except ValueError as error_message:
			wx.MessageBox("Error de conexion","Error", wx.OK | wx.ICON_ERROR) 

	def checkLimit(self):
		data = api.rate_limit_status()
		limit = data['resources']['search']['/search/tweets']['remaining']
		utc = int(data['resources']['search']['/search/tweets']['reset'])
		if limit > 20:
			return True
		else:
			a = datetime.fromtimestamp(utc, pytz.timezone('America/Mexico_City'))
			wx.MessageBox("Limite excedido intente de nuevo despues de las: "+str(a),"Error", wx.OK | wx.ICON_ERROR)




 consumer_key = 'YOUR_COSTUMER_KEY'
 consumer_secret = 'YOUR_COSTUMER_SECRET_KEY'
 access_token = 'YOUR_ACCESS_TOKEN'
 access_secret = 'YOUR_ACCESS_SECRET_TOKEN'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)






