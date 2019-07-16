import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def topFiveByIndustry(industry): 
    
    result = collection.aggregate([ {"$match": {"Industry": industry }}, { "$sort": { "Price": -1}}, {"$limit": 5}, { "$project" : { "Ticker" : 1 , "Price" : 1, "_id": 0 } }])

    return result
  
