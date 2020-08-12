from bs4 import BeautifulSoup
#學習和使用 find_all()方法
with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 找出前2個問卷的題目清單
tag_list = soup.find_all("p", class_="question", limit=2) #方法:find_all(self, name=None, attrs={}, recursive=True, text=None,limit=None, **kwargs)
print(tag_list) #find_all回傳資料形式為 list 串列
print('-------------')
print(tag_list[0]) #取得第0筆
print(type(tag_list)) #資料型態 <class 'bs4.element.ResultSet'>
print(len(tag_list)) #串列長度 2
for question in tag_list: #使用迴圈取得資料
    print(question.a.string)
