from bs4 import BeautifulSoup

html_str = "<div id='msg' class='body strikeout'>Hello World!</div>"
soup = BeautifulSoup(html_str, "html.parser")
tag = soup.div
print(tag.string)        # 內容
print(type(tag.string))  # tag的 string型態