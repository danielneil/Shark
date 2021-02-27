#!/usr/bin/python3

from pydrill.client import PyDrill

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

test_json = drill.query('''
  SELECT * FROM
  `dfs.root`.`/shark/backtest/tradelog/`
''')

for result in test_json:
    print("%s: %s" %(result['ticker'], result['quantity']))
