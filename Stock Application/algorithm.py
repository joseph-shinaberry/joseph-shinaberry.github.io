import json
import requests
import datetime
from bson import json_util
from pymongo import MongoClient

now = datetime.datetime.now()
formatDate = now.strftime("%Y-%m-%d")

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']



def getLiveStockData(ticker):

	''' getLiveStockData grabs the data from stock data live from alpha vantage and imports 
	the live stock price into the application. This uses an outside API that requires a unique key '''

	apikey = 'SO86DECTV0CVLVH5'
	result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey=' + apikey)


	if result.status_code != 200: 
		
		result = "Somthing went wrong"
	
	else:
		
		result = result.json()

	return result


def compareLiveStockToStored(ticker):

	''' compareLiveStockStored gets the live stock data from getLiveStockData and compares it will the stored
	data from a mongodb database. '''

	#dictionary data structures 
	dictStructTicker = {"Ticker" : ticker}
	dictStructReturn = {"Price": 1, "_id": 0 }
	
	#mongodb query
	stored = collection.find_one(dictStructTicker, dictStructReturn)
	

	live = getLiveStockData(ticker)
	livePrice = live['Time Series (Daily)'][formatDate]['1. open']
   	
   	if stored['Price'] > livePrice:
   		#todo chage stored price to something compairable 
	    	result = "Stock Price is now lower than stored - Stored: " + str(stored['Price']) + " Live " + str(livePrice)

    	else:

			result = "Stock Price is now higher than stored - Stored: " + str(stored['Price']) + " Live " + str(livePrice)

    	return result


#test main // to be deleted later. 
def main():
	
	print compareLiveStockToStored('A')

main()
