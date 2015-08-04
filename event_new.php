		  <?php
			//Start session and get the database connection details
			session_start(); 
			include 'data.php';
			include 'Geocode.php';
			
			use kamranahmedse\Geocode;

			$errMsg_arr = array(); $errFlag = false;
			
			//Connect to the uni database
			$link = mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
			if(!$link){
				die('Failed to connect to server: ' . mysql_error());
			}
			
			//Select database
			$db = mysql_select_db(DB_DATABASE);
			if(!$db){
				die("Unable to select database");
			}
			
			$name = $_POST['name'];
			$date = $_POST['date'];
			$time = $_POST['time'];
			$address = $_POST['address'];
			//$latitude = $_POST['latitude'];
			//$longitude = $_POST['longitude'];
			
			if($name == ''){
				$errMsg_arr[] = 'Missing event name';
				$errFlag = true;
			}
			
			if($date == ''){
				$errMsg_arr[] = 'Missing event date';
				$errFlag = true;
			}
			
			if($time == ''){
				$errMsg_arr[] = 'Missing event time';
				$errFlag = true;
			}
			if($address == ''){
				$errMsg_arr[] = 'Missing event time';
				$errFlag = true;
			}
			
			$geocode = new Geocode( $address );
			
			$latitude = $geocode->getLatitude(); // returns the latitude of the address
			$longitude = $geocode->getLongitude(); // returns the longitude of the address
		/*	if($longitude == '') {
				$errMsg_arr[] = 'Missing event latitude';
				$errFlag = true;
			}
			if($latitude == '') {
				$errMsg_arr[] = 'Missing event longitude';
				$errFlag = true;
			}
			*/
			if($name != ''){
				$qry = "SELECT * FROM events WHERE name='$name'";
				$result = mysql_query($qry);
				if($result){
					if(mysql_num_rows($result) > 0) {
						$errMsg_arr[] = 'event name already exists';
						$errFlag = true;
					}
				}
			}
			
			if($errFlag){
				$_SESSION['ERRMSG_ARR'] = $errMsg_arr;
				session_write_close();
				header("location: register.php");
				exit();
			}
			
			$qry = "INSERT INTO events (name, date, time, latitude, longitude, address) VALUES ('$name', '$date', '$time', '$latitude', '$longitude', '$address')";
			
			$result = mysql_query($qry);
			
			
				//Redirect to here if result is successful
			if($result){
				header("location: map_test.php");
				exit();
			} else{
				echo "hey";
				die("Query failed");
			}
		?>




