from bs4 import BeautifulSoup
from bs4.element import NavigableString
#加入指針在尾部
soup = BeautifulSoup("<b></b>", "html.parser")    
tag = soup.b
tag.append("Joe") #加入 append()
print(tag)
new_str = NavigableString(" Chen") #定義 html 標籤 Chen
tag.append(new_str) #加入
print(tag)
new_tag = soup.new_tag("a", href="http://www.example.com") #創建 <a href="http://www.example.com">
tag.append(new_tag) #加入
print(tag)