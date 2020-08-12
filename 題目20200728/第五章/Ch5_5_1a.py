from bs4 import BeautifulSoup
from bs4.element import NavigableString
#調用類別 NavigableString (html標籤)
with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用childen屬性取得子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>
for child in tag_ul.children:
    if not isinstance(child, NavigableString): #加入 isinstance()過濾多餘的物件
        print(child.name)