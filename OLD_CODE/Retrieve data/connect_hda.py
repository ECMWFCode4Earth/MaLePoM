from hda import Client
# importing the module
import json


c = Client(debug=True)


  
# Opening JSON file
with open('query.json') as json_file:
  query = json.load(json_file)

  matches = c.search(query)
  print(matches)
  matches.download()