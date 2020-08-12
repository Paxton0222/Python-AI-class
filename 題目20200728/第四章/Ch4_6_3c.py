from bs4 import BeautifulSoup

html_str = "<div id='msg'>Hello World!</div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div 
print(tag)
print(soup.name) #顯示BeautifulSopu屬性
print(type(soup))   # BeautifulSoup型態

