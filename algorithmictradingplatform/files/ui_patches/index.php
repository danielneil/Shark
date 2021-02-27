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
#!/usr/bin/python3

from pydrill.client import PyDrill

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

test_json = drill.query('''
  SELECT * FROM
  `dfs.root`.`/home/daniel/Shark/apache-drill/files/testFile.json`
  LIMIT 1
''')

for result in test_json:
    print("%s: %s" %(result['ticker'], result['quantity']))

