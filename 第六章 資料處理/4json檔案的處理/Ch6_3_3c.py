import requests
from bs4 import BeautifulSoup
#找到GOOGLE LOGO 的 HTML
url = "http://www.google.com.tw"
r = requests.get(url)
r.encoding = "big5"
soup = BeautifulSoup(r.text, "html.parser")
tag_a = soup.find(id="hplogo")
print(tag_a)