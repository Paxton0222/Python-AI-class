from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
print(tag_ul)
print('-------------')
# 使用屬性取得所有祖先標籤
for tag in tag_ul.parents: #上訪
    print(tag.name)
# 使用函數取得所有祖先標籤
print('-------------')
for tag in tag_ul.find_parents():
    print(tag.name)