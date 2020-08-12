import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df2 = df.set_index(["city", "name"]) #設定索引
df2.sort_index(ascending=False, inplace=True) #呼叫索引的排序方式是由大到小 ascending 代表升序 inplace代表適當修改 dataframe
print(df2)
df2.to_html("Ch9_2_5a.html")