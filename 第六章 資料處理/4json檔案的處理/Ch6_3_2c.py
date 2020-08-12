import json
import requests

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
jsonfile = "Books.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
print(json_data)
with open(jsonfile, 'w') as fp:
    json.dump(json_data, fp)