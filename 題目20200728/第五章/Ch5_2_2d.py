from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

tag_div = soup.find("div", id="q2")
# 找出所有<p>和<span>標籤
tag_list = tag_div.find_all(["p", "span"]) #指定所有標籤 <p> <span> 回傳
print(tag_list)
# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"]) #找尋參數 class="question" and class="selected"
print(tag_list)

