import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen') #定義cookies
r = requests.get(url, cookies=cookies) #傳送cookies
print(r.text) #顯示文字
