from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

tag_div = soup.find("div", id="q2")
# 找出所有文字內容清單
tag_str_list = tag_div.find_all(text=True) #只有文字才回傳
print(tag_str_list)
# 找出指定的文字內容清單
tag_str_list = tag_div.find_all(text=["20", "40"]) #指定搜尋文字內容回傳
print(tag_str_list)

