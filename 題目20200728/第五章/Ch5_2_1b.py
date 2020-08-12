from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用class屬性搜尋<span>標籤
tag_span = soup.find(attrs={"class": "score"}) #搜尋 class="score" 的 html 第一種方法
print(tag_span.string)
# 搜尋第2題的第1個<span>標籤
tag_div = soup.find(id="q2")
tag_span = tag_div.find(class_="score") #搜尋 class="score" 的 html 第二種方法 
#為何是 class_ ? 因為 class 是 Python 中的關鍵字，故使用 _ 迴避
print(tag_span.string)

