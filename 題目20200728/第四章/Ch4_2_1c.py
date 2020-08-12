import requests

data = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=data) #傳送資料給網站
print(r.url) #顯示get方法中 get 參數
print(r.text)