from bs4 import BeautifulSoup

soup = BeautifulSoup("<p><b>One</b></p>", "html.parser")  
tag = soup.b  
new_tag = soup.new_tag("i") #更改 tag > <i>
new_tag.string = "Two" #創建 str "Two"
tag.replace_with(new_tag) #跟 <i> 的文字做替換
print(soup.p)