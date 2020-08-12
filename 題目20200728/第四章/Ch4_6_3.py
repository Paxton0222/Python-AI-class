from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikeout'>Hello World!</div>"
soup = BeautifulSoup(html_str, "html.parser")
tag = soup.div
print(type(tag))     # Tag型態
print(tag.name)      # tag的 html 名稱
print(tag["id"])     # tag 的 id
print(tag["class"])  # 多重值屬性的值清單
print(tag.attrs)     # 標籤所有屬性值的字典