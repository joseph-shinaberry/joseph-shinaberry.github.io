import json
from bson import json_util
from pymongo import MongoClient
import datetime

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#insert into database 
def insert_mongodb(document): 
    try: 
      result = collection.insert_one(document)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result


#read database entry
def read_mongodb(document): 
    try: 
      result = collection.find_one(document)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result


#update database entry
def update_mongodb(find, update): 
    try: 
      result = collection.update_many(find, update)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result

#delete  database 
def delete_mongodb(document): 
    try: 
      result = collection.delete_many(document)
    
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result