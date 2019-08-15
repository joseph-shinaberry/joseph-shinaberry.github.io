<?php
//This file is ran only once to create the tables upon installation of the app to the server.
//Purpose: Create tables to be imported into the database. 

include "database.php";

$sql = "CREATE TABLE Stocks (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
ticker VARCHAR(30) NOT NULL,
price VARCHAR(30) NOT NULL,
volume VARCHAR(50),
date_entered TIMESTAMP
)";


echo create_tables($conn, $sql);


