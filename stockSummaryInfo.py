import json
from bson import json_util
from pymongo import MongoClient


connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def stockSummaryInfo(ticker): 
    try: 
      result = collection.find({"Ticker" : ticker}, {"Ticker": 1, "Price": 1, "Volume": 1, "50-Day Simple Moving Average": 1, "_id": 0 })
      
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result

    

