from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

tag_div = soup.find("div", id="q2")
# 找出所有標籤清單
tag_all = tag_div.find_all(True) #參數值為True，有資料就回傳
print(tag_all)