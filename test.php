<html>
<head>
</head>
<body>

<form action="" >
nono
</form>

<?php

function login($username, $password, $db){
    


}

$connection = new Mongo();

$db = $connection->selectDB('cubedb');

$collection = $db->users;

$doc_cursor = $collection->find();

foreach ($doc_cursor as $doc) {
    foreach ($doc as $key => $val){
        echo $key . ': ' . $val . '<br>';
}
}

?>
</body>
</html>
