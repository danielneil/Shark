#!/usr/bin/python3

import jaydebeapi
import jpype
import os
import pandas as pd

drill_home = '/shark/apache-drill/apache-drill-1.18.0'

classpath = [ 
            drill_home + '/jars',
            drill_home + '/jars/thirdparty'
        ]

jpype.startJVM("-ea", 

conn = jaydebeapi.connect(
    'org.apache.drill.jdbc.Driver',
    'jdbc:drill:drillbit=localhost'
)

cursor = conn.cursor()

query = """
    SELECT *
    FROM dfs.`./testFile.json`
    LIMIT 1
"""

cursor.execute(query)
columns = [c[0] for c in cursor.description]
data = cursor.fetchall()
df = pd.DataFrame(data, columns=columns)

df.head()
