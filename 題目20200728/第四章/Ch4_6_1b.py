from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    print(soup)