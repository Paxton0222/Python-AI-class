from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
tag_html = soup.html # 找到第<html>標籤
print(type(tag_html), tag_html.name) #html
tag_next = tag_html.next_element.next_element
print(type(tag_next), tag_next.name) #head
tag_title = soup.title # 找到第<title>標籤
print(type(tag_title), tag_title.name)
tag_previous = tag_title.previous_element.previous_element #meta charset
print(type(tag_previous), tag_previous.name)
