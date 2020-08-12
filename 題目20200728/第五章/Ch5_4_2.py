import re #正規表示式模組
from bs4 import BeautifulSoup
#使用正規表示式過濾文字
#推薦測試網站 https://pythex.org/
with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用正規運算式搜尋文字內容
tag_str = soup.find(text="男 -") #選擇文字裡帶有 "男 -"" 的
print(tag_str)
regexp = re.compile("男 -")  #建立正規表示式物件
tag_str = soup.find(text=regexp) #把 regexp 帶入text參數
print(tag_str)
regexp = re.compile("\w+ -") #\w+ - 代表所有文字可以出現1次或很多次
tag_list = soup.find_all(text=regexp)
print(tag_list)