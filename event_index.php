<!DOCTYPE html>

<html>
<head>
<title>Maps Login</title>
<link rel="stylesheet" type="text/css" href="Style.css" />
</head>
<body>
	<h1>Hey</h1>
	<iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/place?q=ann%20arbor&key=AIzaSyDM7Kx1IT9MKWzmjSc9BwZhdRB2FI_pRYs"></iframe>
	<nav>
		<form action="event_new.php" method="post">
			<ul>
				<!--<li><a href=login_customer.php>Customer Login</a></li>
				<li><a href=register.php>Register</a></li>-->
				<input id = "name" name = "name" type = "text" placeholder = "Enter Name"/>
				<input id = "date" name = "date" type = "text" placeholder = "Enter Date"/>
				<input id = "time" name = "time" type = "text" placeholder = "Enter Time"/>
				<input id = "address" name = "address" type = "varchar" placeholder = "Enter Address"/>
			<!--	<input id = "latitude" name = "latitude" type = "double" placeholder = "Enter Latitude"/>
				<input id = "longitude" name = "longitude" type "double" placeholder = "Enter Longitude"/>-->
			</ul>
		<input type="submit" name="submit" value="Check In" />
	</nav>	
</body>
</html>