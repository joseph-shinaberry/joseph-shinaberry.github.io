import json
from bson import json_util
from pymongo import MongoClient
import pprint

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def read_mongodb(document): 
    try: 
      result = collection.find_one(document)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result
  
def main():
  
  mydict = { "Ticker": "A" }
  
  pprint.pprint(read_mongodb(mydict))
  
main()

