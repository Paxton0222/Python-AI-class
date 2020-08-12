from bs4 import BeautifulSoup
#修改 Html網頁
soup = BeautifulSoup("<b class='score'>Joe</b>", "html.parser")    
tag = soup.b
print(tag)
tag.name = "p" #更改 tag 為 <p>
tag["class"] = "question" # class='score' > class='question'
tag["id"] = "name" #沒有就自創一個
print(tag)
del tag["class"] #刪除 Class
print(tag)   