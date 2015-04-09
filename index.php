<?php

function login($username, $password){
	$connection = new Mongo();

	$db = $connection->selectDB('cubedb');

	$collection = $db->users;

	$doc = $collection->findOne( array('username' => $username, 'password' => $password) );
	//doc null if no result found

	if ($doc){
		//echo $doc["_id"];
		return true;
	}
	
	return false;
	
}

$login = false;
if (isSet($_POST["username", $_POST["password"])){
	$username = $_POST["username"];
	$password = $_POST["password"];
	
	if( login($username, $password) )
		$login = true;
} 
	
if (!$login){
	header('Location: /login.php');
}

require_once("/resources/header.php");

echo "<div> Logged in as " . $username . </div>;

require_once("/resources/footer.php");

?>

