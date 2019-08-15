<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$msg = "";

if($_SERVER['REQUEST_METHOD'] == 'POST'){

		include "database.php";
		$apikey = "SO86DECTV0CVLVH5";

		$ticker = $_POST['ticker'];
		$volume = $_POST['volume'];

		$result = file_get_contents("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=".$ticker."&apikey=" . $apikey);

		$result_strings  = json_decode($result);

		if (isset($result_strings->{'Global Quote'}->{'05. price'})){

		$price = $result_strings->{'Global Quote'}->{'05. price'};



		update($conn, $ticker, $volume, $price);

		 
		$msg = "Success";
		}else{

			$msg = "Fail";

		}
}

?>
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Stock App Update</title>

   
  </head>
  <body>
  	<!-- Navbar -->
	 <nav class="navbar navbar-expand-lg navbar-light bg-light">
	  <a class="navbar-brand">Stock Market Application</a>
	  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
	    <span class="navbar-toggler-icon"></span>
	  </button>
	  <div class="collapse navbar-collapse" id="navbarNav">
	    <ul class="navbar-nav">

	      <li class="nav-item">
	        <a class="nav-link" href="index.php">Create Ticker</a>
	      </li>
	      <li class="nav-item">
	        <a class="nav-link" href="read.php">Read Ticker</a>
	      </li>
	      <li class="nav-item">
	        <a class="nav-link" href="update.php">Update Ticker</a>
	      </li>
	      <li class="nav-item">
	        <a class="nav-link" href="delete.php">Delete Ticker</a>
	      </li>
	    </ul>
	  </div>
	</nav>
	<!-- Navbar End -->
  	<div class="container">
  		<br>
  		<div class="row">
	    	<div class="card">
			  <div class="card-body">
			  <p> Welcome to the stock application, this application is a simple application to store stock market tickers into a database with the price and purchased volume.</p> <p> To get started you may enter a stock ticker followed by the volume purchased and it will grab the current price and place it into the database </p>
			  </div>
			</div>
		</div>


		<br>
		<?php if ($msg == "Success"){ echo'<div class="alert alert-success">
  <strong>Success! </strong>Stock Price for <br> Ticker: '.$ticker.' <br> Price: $'.$price.'
</div>';}?>
<?php if ($msg == "Fail"){ echo'<div class="alert alert-danger">
  <strong>ALERT! </strong>Stock Price for Ticker: '.$ticker.' Does not exist!
</div>';}?>

			<form method="post" action="update.php" enctype="multipart/form-data">
			  <div class="form-row">
			    <div class="col">
			      <input type="text" class="form-control" name="ticker" placeholder="Ticker Symbol">
			    </div>
			    <div class="col">
			      <input type="number" class="form-control" name="volume" placeholder="Volume Purchased (Total Shares)">
			    </div>
			  </div>
			  <br>
			  <center>
			  	<input class="btn btn-primary btn-lg" type="submit" value="Submit">
				<input class="btn btn-primary" type="reset" value="Reset">
				</center>
			</form>
		


























	</div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>

