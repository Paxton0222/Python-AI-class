import requests

"""
proxies = {
"https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print(r.text)
"""
#  main
r = requests.get("http://www.google.com.tw")
#print(r.text) #取得文本式數據 Unicode
print("----------------------")

r = requests.get("http://www.google.com.tw")
#print(r.content) #取得二進制代碼 bytes 數據
#print("----------------------")

r = requests.get("http://www.google.com.tw", stream=True) #原始socket回應 stream=True
#print(r.raw) #<urllib3.response.HTTPResponse object at 0x0342B550>
print(r.raw.read(15)) #b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xddo\xdc'

