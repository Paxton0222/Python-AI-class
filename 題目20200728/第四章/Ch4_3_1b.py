import requests

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

r = requests.get("http://httpbin.org/user-agent"),#headers = headers)
print(r.text)
print(type(r.text)) #資料型態
print("----------------------")
print(r.json()) 
print(type(r.json())) #資料型態


