<?php

	function printDate() {
		echo  date("l jS \of F Y h:i:s A");
	}

	echo "<h1> This webpage has a single line that dynamically changes, so it should be ignored by the plugin, but the checksum should remain the same.</h1>";

	echo "<h2>This line changes: " . printDate() . "</h2>";

	echo "<h2>This line doesn't change</h2>";
?>
