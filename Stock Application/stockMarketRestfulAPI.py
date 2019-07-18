#!/usr/bin/python
import json
from bson import json_util
from bson.json_util import dumps
import bottle
from pymongo import MongoClient
from bottle import route, run, request, abort
import datetime
import pprint

from algorithm import compareLiveStockToStored

#custom imports for CRUD updates
from database import insert_mongodb, read_mongodb, update_mongodb, delete_mongodb



#////////////////////////////////////Algorithm API URI\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Route curl http://localhost:8008/compare?ticker="A"
@route('/compare', method='GET')
def get_compare():
  try:
    ticker=request.query.ticker
    if ticker: 
      entity = compareLiveStockToStored(ticker)
    if not entity:
        abort(404, 'No document with id %s' % id)
  except NameError:
    abort(404, "No parameter")
  return json.loads(json.dumps(entity, indent=4, default=json_util.default))

  

#////////////////////////////////////CRUD API URI\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Route curl -H "Content-Type: application/json" -X POST -d '{"Ticker" : "SNHU", "Profit Margin" : 0.137, "Sector" : "Healthcare", "Shares Outstanding" : 339, "Price" : 50.44, "Industry" : "Medical Laboratories & Research", "Company" : "Southern New Hampshire University", "Volume" : 1847978, "50-Day Simple Moving Average" : -0.0055}' http://localhost:8008/create

@route('/create', method='POST')
def post_mongodbCreate():
  data = request.body.readline() 
  if not data:
    abort(400, 'No data received') 
  entity = json.loads(data)
  if not entity.has_key('Ticker'):
    abort(400, 'No ticker specified') 
  try:
    result = insert_mongodb(entity)
    result = "{ \"Insert\": \"Success\" }"
  except ValidationError as ve:
    abort(400, str(ve))
  return json.loads(json.dumps(result, indent=4, default=json_util.default))  + "\n"


# Route curl http://localhost:8008/read?ticker="A"
@route('/read', method='GET')
def get_mongodbResult():
  try:
    ticker=request.query.ticker
    if ticker: 
      entity = read_mongodb({ "Ticker": ticker })
    if not entity:
        abort(404, 'No document with id %s' % id)
  except NameError:
    abort(404, "No parameter")
  return json.loads(json.dumps(entity, indent=4, default=json_util.default))


# Route curl http://localhost:8008/update?ticker="SNHU"\&volume="444"
@route('/update', method='GET')
def get_mongodbUpdate():
  try:
    ticker = request.query.ticker
    volume = request.query.volume
    if ticker and volume: 
      find = { "Ticker": ticker }
      update = { "$set": { "Volume": volume } }
      entity = update_mongodb(find, update).modified_count
      result="{ \"Updated\": \""+str(entity)+"\" }"
    else:
      result="{ \"Error\": \""+requested_result+"\" }"
  except NameError:
    abort(404, "No parameter")
  return json.loads(json.dumps(result, indent=4, default=json_util.default))  + "\n"


# Route curl http://localhost:8008/delete?ticker="SNHU"
@route('/delete', method='GET')
def get_mongodbDelete():
  try:
    ticker=request.query.ticker
    if ticker: 
      find = { "Ticker": ticker }
      entity = delete_mongodb(find)
      result="{ \"deleted\": "+str(entity.deleted_count)+" }"
    if not entity:
        abort(404, 'No document with ticker %s' % id)
  except NameError:
    abort(404, "No parameter")
  return json.loads(json.dumps(result, indent=4, default=json_util.default))  + "\n"






'''Starts the RESTful API on listening on port 8008'''

if __name__ == '__main__': #declare instance of request
    #app.run(debug=True)
    run(host='localhost', port=8008)

