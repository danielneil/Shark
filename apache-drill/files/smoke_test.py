#!/usr/bin/python3
from pydrill.client import PyDrill

drill = PyDrill(host='localhost', port=8047)

if not drill.is_active():
    raise ImproperlyConfigured('Please run Drill first')

yelp_reviews = drill.query('''
  SELECT * FROM
  `dfs.root`.`./Users/macbookair/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json`
  LIMIT 5
''')

for result in yelp_reviews:
    print("%s: %s" %(result['type'], result['date']))


# pandas dataframe

df = yelp_reviews.to_dataframe()
print(df[df['stars'] > 3])
