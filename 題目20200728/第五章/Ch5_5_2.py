from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性向下走訪
print(soup.html.head.title.string) #找到 html > head > title 的文字
print(soup.html.head.meta["charset"]) #找到 html > head > title > meta["charset"]
# 使用div屬性取得第1個<div>標籤
print(soup.html.body.div.div.p.a.string) #找到 html > body > div > div > p > a 的文字