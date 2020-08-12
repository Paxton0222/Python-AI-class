from bs4 import BeautifulSoup
#學習和使用 css 選擇器 5-18
with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 搜尋<title>標籤和第3個<div>標籤
tag_title = soup.select("title")
print(tag_title[0].string)
tag_first_div = soup.find("div")
#print(tag_first_div)
tag_div = tag_first_div.select("div:nth-of-type(3)") #在所有 div 標籤中 選擇第3個 5-20
print(tag_div[0])


