<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

//This is the main database file that is designed to handled all the database functions in a single file.



$servername = "localhost";
$username = "diesel";
$password = "SAJN39oA8VqsAQHG";
$database = "stock_app";

$conn = mysqli_connect($servername, $username, $password, $database);

if ($conn->connect_error){
	die ("Connection Failed, Error: ". $conn->connect_error);
}


function create_tables($conn, $sql){

	mysqli_query($conn, $sql);


}

function create($conn, $ticker, $volume, $price){

	$sql = "INSERT INTO Stocks (ticker, volume, price) VALUES ('".$ticker."','".$volume."','".$price."')";

	mysqli_query($conn, $sql);

}

function read($conn, $ticker){

	$sql = "SELECT * FROM Stocks WHERE ticker = '".$ticker."'";

	return mysqli_query($conn, $sql);
}

function read_all($conn){

	$sql = "SELECT * FROM Stocks";

	$result = mysqli_query($conn, $sql);

	return $result;

}

function update($conn, $ticker, $volume, $price){

	$sql = "UPDATE Stocks SET volume = " .$volume . " , price = ".$price."  WHERE ticker = '".$ticker."'";

	mysqli_query($conn, $sql);
}

function delete($conn, $ticker){

	$sql = "DELETE FROM Stocks WHERE ticker = '".$ticker."'";

	mysqli_query($conn, $sql);
}



?>


