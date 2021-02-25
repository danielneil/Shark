#!/usr/bin/python3

from pydrill.client import PyDrill

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

yelp_reviews = drill.query('''
  SELECT * FROM
  `dfs.root`.`/home/daniel/Shark/apache-drill/files/testFile.json`
  LIMIT 1
''')

for result in yelp_reviews:
    print("%s: %s" %(result['ticker'], result['quantity']))

