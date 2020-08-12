from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.string) #p > a >文字
print("-----------")
tag_div = soup.select("#q1 ~ .survey") #id="q1" 所有後面的  class="survey" 5-19
for item in tag_div:            
    print(item.p.a.string)  
print("-----------")
tag_div = soup.select("#q1 + .survey") #id="q1" 後面的第一個 class="survey" 5-19
for item in tag_div:            
    print(item.p.a.string)   


