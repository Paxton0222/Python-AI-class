from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用屬性取得所有子孫標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
print(tag_ul.descendants)
for child in tag_ul.descendants: #取得所有的 html標籤
    if not isinstance(child, NavigableString):#判斷是否為NavigableString
        print(child.name) #html標籤