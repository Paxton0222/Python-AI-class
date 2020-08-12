import re
from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用正規運算式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+") #搜尋email的正規表示式 這裡給另一種寫法 : [a-zA-Z0-9_]+@[a-zA-Z0-9\.]+ "."代表除了(\n)以外所有字元
#"\"代表後面字元以一般字元處理
tag_str = soup.find(text=email_regexp)
print(tag_str)
print("---------------------")
tag_list = soup.find_all(text=email_regexp)
print(tag_list)