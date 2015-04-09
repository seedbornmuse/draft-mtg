<?php
require_once("resources/templates/header.php");
?>

<div id="login">
	<form method="POST" action="index.php">
		Username: <input type="text" name="username"> <br>
		Password: <input type="password" name="password">
		<input type="submit" value="Submit">
	</form>

</div>

<?php
require_once("resources/templates/footer.php");
?>
