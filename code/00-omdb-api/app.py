import urllib
import json

data = json.loads(urllib.urlopen('http://www.omdbapi.com/?t=Game%20of%20Thrones&Season=1').read())

for episode in data['Episodes']:
  print episode['Title']

