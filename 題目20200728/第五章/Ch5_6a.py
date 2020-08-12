from bs4 import BeautifulSoup

soup = BeautifulSoup("<b class='score'>Joe</b>", "html.parser")    
tag = soup.b
tag.string = "Mary" # Joe > Mary
print(tag)