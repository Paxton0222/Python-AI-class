from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 搜尋class和id屬性值的標籤
tag_div = soup.select("#q1") #id='q1'
print(tag_div[0].p.a.string) #第0個 p > a > 文字
tag_span = soup.select("span#email") #標籤 span id="email"
print(tag_span[0].string) #第 0 個 文字
tag_div = soup.select("#q1, #q2")  # 多個id屬性
for item in tag_div:
    print(item.p.a.string)
print("-----------")
tag_div = soup.find("div")  # 第1個<div>標籤
tag_p = tag_div.select(".question") # class="question"
for item in tag_p:
    print(item.a["href"])
tag_span = soup.select("[class~=selected]") #class="selected" 所有後面的 ~= 包括自己
for item in tag_span:
    print(item.string)
