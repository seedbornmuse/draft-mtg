<?php

//if (isSet($_POST["username", $_POST["password"])){
$username = $_POST["username"];
$password = $_POST["password"];
//}



$connection = new Mongo();

$db = $connection->selectDB('cubedb');

$collection = $db->users;

//$cursor = $collection->find( array('username' => $username, 'password' => $password) );

function login($username, $password, $db){


}
$doc = $collection->findOne( array('username' => $username, 'password' => $password) );
//doc null if no result found

if ($doc){
	session_start();
}

if ($doc){
	echo $doc["_id"];
}

/*foreach ($doc_cursor as $doc) {
    foreach ($doc as $key => $val){
        echo $key . ': ' . $val . '<br>';
		
}
}*/
/*
while ( $cursor->hasNext() )
{
    var_dump( $cursor->getNext() );
}
*/

?>
</body>
</html>
