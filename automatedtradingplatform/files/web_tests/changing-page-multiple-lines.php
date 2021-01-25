<?php

	function printDate() {
		return date("l jS \of F Y h:i:s A");
	}

	echo "<h1> This webpage has multiple lines it in that dynamically change, so they should be ignored by the plugin, but the checksum should remain the same.</h1>";

	echo "<h2>This line changes: " . printDate() . "</h2>";

	echo "<h2>This line doesn't change</h2>";

	echo "<h2>This line changes: " . printDate() . "</h2>";

	echo "<h2>This line doesn't change</h2>";

	echo "<h2>This line changes: " . printDate() . "</h2>";

	echo "<h2>This line doesn't change</h2>";
?>
