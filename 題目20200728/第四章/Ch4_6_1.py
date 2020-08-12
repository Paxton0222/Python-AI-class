from bs4 import BeautifulSoup #使用外部函數庫 bs4 模組
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/   bs4 official webpage
html_str = "<p>Hello World!</p>" #html
soup = BeautifulSoup(html_str, "html.parser") #使用類別 BeautifulSoup(markup="","html.parser") 取得 html_str 中的資料  
#並使用 python的 html.parser 解析器
print(soup)
#lxml，lxml-xml 具有執行速度快的優點，但必須安裝 C 語言，故不在此使用。
#另外還有html5lib解析器，容錯能力強，不會亂刪東西