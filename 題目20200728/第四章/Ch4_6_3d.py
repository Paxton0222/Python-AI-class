from bs4 import BeautifulSoup

html_str = "<p><!-- 註解文字 --></p>"
soup = BeautifulSoup(html_str, "html.parser")
comment = soup.p.string #取得p中的文字
print(comment)
print(type(comment))   # Comment型態

