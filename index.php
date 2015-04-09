<?php

function login($username, $password){
	$connection = new Mongo();

	$db = $connection->selectDB('cubedb');

	$collection = $db->users;

	$doc = $collection->findOne( array('username' => $username) );
	//doc null if no result found

	if ($doc){
		if ($doc['password'] == $password){ //check if password matches
			return true;
		} 
		else if ($doc['session'] == $session){
			return true;
		}
	}
	
	return false;
	
}

$login = false;
if (isSet($_POST["username"], $_POST["password"])){
	$username = $_POST["username"];
	$password = $_POST["password"];
	
	if( login($username, $password) )
		$login = true;
} 
	
if (!$login){
	header('Location: login.php');
}

require_once("resources/templates/header.php");

?>

<div>Logged in as <?=$username?></div>

<form action="" method="POST">
	<input type="submit" value="Host Draft">
	<input type="submit" value="Join Draft">
</form>

<?

require_once("resources/templates/footer.php");

?>

