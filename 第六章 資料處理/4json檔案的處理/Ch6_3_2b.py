import json

jsonfile = "Example.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp) #轉換成字典
json_str = json.dumps(data) #轉換成字串
print(json_str)
print(type(json_str))