from bs4 import BeautifulSoup

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 搜尋特定屬性值的標籤
tag_a = soup.select("a[href]") #選擇所有 a href
#print(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']") #選擇 q2
#print(tag_a)
tag_a = soup.select("a[href^='http://example.com']")  #選擇所有開頭帶有 http://example.com 
print(tag_a)
tag_a = soup.select("a[href$='q3']") #選擇所有屬性結尾是 q3
#print(tag_a)
tag_a = soup.select("a[href*='q']") #選擇所有屬性包含q的
#print(tag_a)