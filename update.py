import json
from bson import json_util
from pymongo import MongoClient
import pprint

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#read database entry
def update_mongodb(find, update): 
    try: 
      result = collection.update_many(find, update)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result
  
  
def main():
  
  find = { "Ticker": "SNHU" }
  
  update = { "$set": { "Volume": "201921" } }
  
  print(update_mongodb(find, update).modified_count, " documents updated")
  print(collection.find_one(find, {"Ticker": 1, "Volume": 1}))