from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "html.parser")  
tag = soup.b  
new_tag = soup.new_tag("i") #更改tag <i>
new_tag.string = "Two" #新增 str "Two"
tag.insert_before(new_tag) #加入在前面
print(soup.p)
new_string = soup.new_string("Three") #新增 str "Three"
tag.insert_after(new_string) #加入在後面
print(soup.p)
tag.clear() #清除 tag --> "b"
print(soup.p)