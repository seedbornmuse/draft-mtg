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

$doc_cursor = $collection->find( array('username' => $username) );

foreach ($doc_cursor as $doc) {
    foreach ($doc as $key => $val){
        echo $key . ': ' . $val . '<br>';
		//var_dump( $doc )
}
}
/*
while ( $cursor->hasNext() )
{
    var_dump( $cursor->getNext() );
}
*/

?>
</body>
</html>
