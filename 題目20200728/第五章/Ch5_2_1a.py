from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用id屬性搜尋<div>標籤
tag_div = soup.find(id="q2") #搜尋 id="q2"
tag_a = tag_div.find("a") #搜尋 "a"
print(tag_a.string)


