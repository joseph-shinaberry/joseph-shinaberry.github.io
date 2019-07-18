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
	apikey = 'SO86DECTV0CVLVH5'
	result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey=' + apikey)


	if result.status_code != 200: 
		
		result = "somehting went wrong"
	
	else:
		
		result = result.json()

	return result


def compareLiveStockToStored(ticker):
	stored = collection.find({"Ticker" : ticker}, {"Price": 1, "_id": 0 })
	#stored = stored.json()

	live = getLiveStockData(ticker)
	livePrice = live['Time Series (Daily)'][formatDate]['1. open']
   	
   	if stored.price > livePrice:
   		#todo chage stored price to something compairable 
	    	result = "Stock Price is now lower than stored - Stored: " + str(stored) + " Live " + str(livePrice)
    	else:
			result = "Stock Price is now higher then stored - Stored: " + str(stored) + " Live " + str(livePrice)

    	return result



def main():
	
	print compareLiveStockToStored('A')

main()
