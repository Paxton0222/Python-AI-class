from bs4 import BeautifulSoup

with open("flag.txt", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser") 
    print(soup.prettify('utf8')) #使用 prettify() 對 html 進行排版
#關於 prettify() 方法 官方文件中說明他會一律輸出utf-8，但是卻是輸出國際碼 unicode 所以這裡建議使用指定邊碼方法
#prettify('utf-8')