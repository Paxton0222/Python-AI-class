import requests
from bs4 import BeautifulSoup
#利用 requests 爬取資料 並用 bs4 執行解析
r = requests.get("https://www.google.com/")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "html.parser") 
print(soup) 