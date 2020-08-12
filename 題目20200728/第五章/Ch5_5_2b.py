from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.children:
    if not isinstance(child, NavigableString): 
        print(child.name) #<li>
        for tag in child:
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string) #不會跑這行
            else:
                print(tag.replace('\n', ''))
#使用replace(oldstr,newstr)方法 