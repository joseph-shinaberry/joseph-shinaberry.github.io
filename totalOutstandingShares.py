import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


#read database entry
def totalOutstandingShares(sector): 
    
    result = collection.aggregate([ {"$match": {"Sector":sector}}, { "$group": { "_id": "$Industry", "Total_Outstanding_Shares": { "$sum": "$Shares Outstanding" } }}])

    return result
  
def main():
  
  sector = "Healthcare"

  cursor = totalOutstandingShares(sector)
  
  for result_object in cursor:
    print result_object
    
main()
