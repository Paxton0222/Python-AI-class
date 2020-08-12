import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.flag.tw") #1.爬蟲
soup = BeautifulSoup(r.text, "html.parser") #2.解析

fp = open("flag2.txt", "w", encoding="utf8") #寫入
fp.write(soup.prettify()) #3.排版
print("寫入檔案flag2.txt...")
fp.close() #4.關閉