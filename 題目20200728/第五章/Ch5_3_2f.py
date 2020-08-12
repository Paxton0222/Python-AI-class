from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用select_one()方法搜尋標籤
tag_a = soup.select_one("a[href]") #只選第一個
print(tag_a)
