# Welcome To Joseph Shinaberry's ePortfolio
## Mission Statement 
Creating something that was not there before, from the spark of imagination -- generated into reality. With each character entered, and with each line saved -- closing in on the ultimate goal to create a solution to make someone’s life easier, more productive, and finally using technology to its fullest potential. My name is Joseph Shinaberry and I am a Software Developer. 

## Self Assessment
>“The secret of getting ahead is getting started. The secret of getting started is breaking your complex overwhelming tasks into small manageable tasks and starting on the first one.” - Mark Twain

Breaking down complex problems into modular and manageable blocks is what an experienced Software Developer such as myself, does on a daily basis. Throughout my journey through the Computer Science program at Southern New Hampshire University, I found that defining a solution for a complex problem was easily managed by breaking down the problem. For Example, a complex mathematical equation may not be solved by starting from left to right but by viewing the entire equation and following the proper order of operations. This is what one must do when creating a software solution, a typical novelist top-down approach is not applicable, and should be substituted for an agile and modular approach. 

The values that I bring to the table are two-fold the first being highly motivated in my field of technology, and the undeterred drive to grow with knowledge in the industry. With the tech industry moving into the future with ever nanosecond staying current on technology is a requirement for any experienced Software Developer. 

Many sets of skills that I have acquired over the term of my experience as well as my time at Southern New Hampshire University include but not limited to; strong collaboration skills, detailed communication, software skills – software engineering, data structures and algorithms, databases, and proficiency in the following languages: PHP, C++, C#, Java, Python, JavaScript, Visual Basic, as well as SQL and NoSQL database language. 

I have collaborated in a team’s requiring many skills including, strong communication, understanding your role, understanding software development lifecycles like Agile with Scrum among others such as Waterfall (iterative development) and Big Bang Model (explosive development) used for smaller teams. 

Furthermore, I have had experience communication the developments to stakeholders, and product owners (Scrum based). This communication required direct, detailed and used little technical acronyms without sparing important elements. Visualizations were often used as shown in the artifacts below to demonstrate the process of the application. 

Below are three artifacts that summarize the talent of software engineering, data structures and database skillset in various different languages. The narrative provides an example of an interaction between developers and ops in a DevOps environment as well as stakeholders. 

## Code Review
<iframe width="560" height="315" src="https://www.youtube.com/embed/8OPQqoeDI14" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


# Artifact 1: Software Engineering / Design
The first artifact is a program known as the Stock Tracker program that was built for CS-340 Advanced Programming Concepts and is a combination of logic, user interface, and NoSQL database structuring. I altered the architecture to all the code to become more modular, the previous architecture of the application contained redundant code that connected to the database from all files. This was a security risk and had to be mitigated by creating a single file that handles database requests. 

### Software Engineering and Design Narrative
![Example of Software Engineer Architecture]({{ site.url }}/imgs/softeng.png)
The idea behind this is to allow the application to become more modular therefore eliminating the need to several different files to perform a single task (accessing the database).

The main [stockMarketRestfulAPI.py](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/d651d7c0849d589b53982400257cb51ebb8c40d7/Stock%20Application/stockMarketRestfulAPI.py#L1-L112) file imports the [database.py](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/dbc5472185c4b1cd8097f48fac7e90f10bd21029/Stock%20Application/database.py#L1-L50) file to import its functions:

```python
#custom imports for CRUD updates
from database import insert_mongodb, read_mongodb, update_mongodb, delete_mongodb
```

***Example of Insert Call From [stockMarketRestfulAPI.py](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/d651d7c0849d589b53982400257cb51ebb8c40d7/Stock%20Application/stockMarketRestfulAPI.py#L1-L112)***
```python
result = insert_mongodb(entity)
```
This allows a single line of code in the main RESTful file, allowing the database file to do the heavy lifting as shown below. 

**Example of Insert Function in [database.py](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/dbc5472185c4b1cd8097f48fac7e90f10bd21029/Stock%20Application/database.py#L1-L50):**
```python
#insert into database 
def insert_mongodb(document): 
    try: 
      result = collection.insert_one(document)
    except ValidationError as ve:
      abort(400, str(ve))
    return result
```
The previous files that had been used to access the database have been created into one single modular file that is both flexible and increases manageability. With a single file that accesses the database allows for increased security, as only one file has access to the database credentials and overall unit testing for database function may be performed on this single file. 


# Artifact 2: Algorithms and Data Structures
The second artifact also uses the Stock Tracker program as a starting point. The enhancements to this application include a data structure that holds JSON data from an external API kindly provided by Alpha Vantage. The live data is then compared to the stored data in the NoSQL database and compares the values with a custom algorithm.

###  Algorithms and Data Structures Narrative
![Example of Algorithm Architecture]({{ site.url }}/imgs/algor.png)

The added algorithms and data structures to the Stock Market app will determine the price of a stock stored to the live price to the stock at the program’s runtime. The API is called to an external service and then compares the prices using an algorithm then storing the information to a dictionary. The final solution is then printed to the screen that can be parsed into Json format. 

***Pulling Data from External API***

The getLiveStockData function in the [algorithm.py](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/6fd05edfd3564d36fae3544466fa73573b165404/Stock%20Application/algorithm.py#L1-L70) file grabs the data from stock data live from alpha vantage and imports the current stock price into the application. This uses an outside API that requires a unique key to connect to the API. 
```python
def getLiveStockData(ticker):
	'''KEY NO LONGER VALID USED AS EXAMPLE'''
	apikey = 'SO86DECTV0CVLVH5' 
	result = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey=' + apikey)

	if result.status_code != 200: 
		result = "Somthing went wrong"
	else:
		result = result.json()
	return result
```
The values are then stored into a data structure for comparison. 

```python
	#dictionary data structures 
	dictStructTicker = {"Ticker" : ticker}
	dictStructReturn = {"Price": 1, "_id": 0 }
```
Data is compaired and logic used to state outcome
```python
	live = getLiveStockData(ticker)
	livePrice = live['Time Series (Daily)'][formatDate]['1. open']
   	
   	if stored['Price'] > livePrice:
   		result = "Stock Price is now lower than stored - Stored: " + str(stored['Price']) + " Live " + str(livePrice)
    	else:
		result = "Stock Price is now higher than stored - Stored: " + str(stored['Price']) + " Live " + str(livePrice)
    	return result
```

# Artifact 3: Databases
The third artifact is an example of the Stock Tracker program completely re-written into a LAMP stack. While the aforementioned artifacts are written in Python & JavaScript with MongoDB as the database. However, the new version is solely written in PHP language and uses MySQL as the database. I will compare the different languages involving database interaction as an example of different database interactions.

###  Database Narrative
For the database portion of the artifact the entire Stock Market app is recoded into a different development stack. Linux, MySQL, Apache and PHP is the chosen stack that the file is recreated in. There is a main database file that handles all interaction with the database as well as create, read, update, and delete functions handled by separate php pages with html. 

***Table Creation***

A schema is used in a relational database such as MySQL this is not used in the previous database type (MongoDB) which is a NoSQL database, therefore for this set up a schema is created.
```php
$sql = "CREATE TABLE Stocks (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
ticker VARCHAR(30) NOT NULL,
price VARCHAR(30) NOT NULL,
volume VARCHAR(50),
date_entered TIMESTAMP
)";
```

***[database.php](https://github.com/joseph-shinaberry/joseph-shinaberry.github.io/blob/61fa6f198eef50c99fa2796aaa1e43ed9be5df3e/Stock%20Application/Stock%20Application%20PHP/database.php#L1-L70) Database - CRUD***
controls all database interaction with Mysql known as CRUD or Create, Read, Update, Delete.

***Create***
```php
function create($conn, $ticker, $volume, $price){
	$sql = "INSERT INTO Stocks (ticker, volume, price) VALUES ('".$ticker."','".$volume."','".$price."')";
	mysqli_query($conn, $sql);
}
```
***Read***
```php
function read($conn, $ticker){
	$sql = "SELECT * FROM Stocks WHERE ticker = '".$ticker."'";
	return mysqli_query($conn, $sql);
}
```

***Update***
```php
function update($conn, $ticker, $volume, $price){
	$sql = "UPDATE Stocks SET volume = " .$volume . " , price = ".$price."  WHERE ticker = '".$ticker."'";
	mysqli_query($conn, $sql);
}
```
***Delete***
```php
function delete($conn, $ticker){
	$sql = "DELETE FROM Stocks WHERE ticker = '".$ticker."'";
	mysqli_query($conn, $sql);
}
```
