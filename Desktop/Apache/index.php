<!DOCTYPE html>

<?php
	if(isset($_POST['submit']))
	{
		$name = $_POST['Name'];
		$email = $_POST['Email'];
		$roomId = $_POST['RoomID'];
		exec("python /var/www/html/spark.py $name $email $roomId");
	}
?>

<html>
	<head>
		<meta charset="utf-8">
		<title>Registration from POC</title>
	</head>
	
	<body>

	<form method="post">
		Name: <br>
		<input type='text' name="Name" /><br>
		Email: <br>
		<input type="text" name="Email" /><br>
		Room: <br>
		<input type="text" name="RoomID" /><br>
		<input type="submit" name="submit" value="submit" /> 

	</form>


	</body>
</html>
