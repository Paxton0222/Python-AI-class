from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 找出所有問卷的題目清單
tag_list = soup.find_all("p", class_="question")
print(tag_list)

for question in tag_list: #使用迴圈 取得 tag_list中的資料
    print(question.a.string)
