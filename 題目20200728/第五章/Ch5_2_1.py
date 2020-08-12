from bs4 import BeautifulSoup
#認識並使用 bs4 的  find() 方法
#find(self, name=None, attrs={}, recursive=True, text=None,**kwargs)
with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")
# 搜尋<a>標籤
tag_a = soup.find("a") #用find方法搜尋"第一個"a 標籤
print(tag_a.string) #顯示文字
# 呼叫多次find()方法
tag_p = soup.find(name="p") #導入參數 "p"
tag_a = tag_p.find(name="a") #導入參數 "a"
print(tag_p.a.string) #顯示文字
print(tag_a.string) #顯示文字
#find()方法只能取得第一個參數