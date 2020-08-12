from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 使用函數建立搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and \
           tag.get("href") == "http://example.com/q2"
#方法:has_attr(markup) 可導入html標籤
#方法:get(markup) 可導入html標籤
tag_a = soup.find(is_secondary_question)
print(tag_a)


