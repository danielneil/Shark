<?php

	function printDate() {
		return date("Y-m-d H:i:s");
	}


	echo "<h1> This webpage has a single line that dynamically changes, so it should be ignored by the plugin, but the checksum should remain the same.</h1>";

	echo "<h2>This line changes: " . printDate() . "</h2>";

	echo "<h2>This line doesn't change</h2>";
?>
