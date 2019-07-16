import json
from bson import json_util
from pymongo import MongoClient


connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def industryLookupTickers(industry): 
    try: 
      result = collection.find({"Industry" : industry}, {"Ticker": 1})
      
    except ValidationError as ve:
      abort(400, str(ve))
    
    return result
  
def main():
  
  industry = "Medical Laboratories & Research"
  
  cursor = industryLookupTickers(industry)
  
  for result_object in cursor:
    print result_object
    
main()
