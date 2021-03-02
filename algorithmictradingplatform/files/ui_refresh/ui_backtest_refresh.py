#!/usr/bin/python3

from pydrill.client import PyDrill

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

tradeCount = drill.query('''
  SELECT count(datetime) FROM
  dfs.tradelog.`SCG.trade.log`
''')

df = tradeCount.to_dataframe()
count = df.iloc[0,0]

print(count)
