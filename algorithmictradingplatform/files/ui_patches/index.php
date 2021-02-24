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
		
		if ( $action == "tradelogs" ) {

			if ( ! strpos($value, '.trade.log' ) ) {
				continue;
			}
		}

		echo "<a href ='$value'>$value</a><br />";
	}
?>
