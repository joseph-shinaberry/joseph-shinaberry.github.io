import json
from bson import json_util
from pymongo import MongoClient


connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def count50DayMoveAvg(low, high): 
    try: 
      result = collection.find({"50-Day Simple Moving Average" : { "$gte": low, "$lt": high }}).count()
      
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result
  
def main():
  
  low = -0.0055
  high = 1
  
  print(count50DayMoveAvg(low, high))
  
main()
