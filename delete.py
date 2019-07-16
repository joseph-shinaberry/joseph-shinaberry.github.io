import json
from bson import json_util
from pymongo import MongoClient
import pprint

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#delete  database 
def delete_mongodb(document): 
    try: 
      result = collection.delete_many(document)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result
  
def main():
  
  findToDelete = { "Ticker": "BRLI" }

  print(delete_mongodb(findToDelete).deleted_count, " documents deleted")
  
