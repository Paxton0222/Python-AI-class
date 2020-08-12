from bs4 import BeautifulSoup

html_str = "<div id='msg'>Hello World! <p> Final Test <p></div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
print(tag.string)        # string屬性
print(tag.text)          # text屬性
print(type(tag.text))  #資料型態
print(tag.get_text())    # 使用get_text()函數
print(tag.get_text('-')) 
print(tag.get_text("-", strip=True)) #刪除前後空白字元