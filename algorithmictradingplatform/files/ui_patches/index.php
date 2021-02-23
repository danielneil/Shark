<?php

	$ticker = $_GET['ticker'];	
	$action = $_GET['action'];

	$directory = ".";

	$files = array_diff(scandir($directory), array('..', '.'));

	foreach ($files as $key => $value) {

		if ( $action == "reports" ) {

			if ( ! strpos($value, '.html' ) ) {
				continue;
			}
		}

		echo "<a href ='$value'>$value</a><br />";
	}
?>
