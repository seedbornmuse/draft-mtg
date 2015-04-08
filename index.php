<html>
<head>
</head>
<body>

<?php

$username = $_POST["username"];
$password = $_POST["password"];

$connection = new Mongo();

$db = $connection->selectDB('cubedb');

$collection = $db->users;

$cursor = $collection->find( array('username' => $username, 'password' => $password) );

var_dump($cursor);

if (cursor::valid()){
	echo cursor->current();
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
