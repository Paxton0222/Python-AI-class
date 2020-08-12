import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

print(df.head()) #head 函數預設是前 5 筆資料
print(df.head(3)) #設定前三筆
df.head().to_html("Ch9_2_3_01.html")
df.head(3).to_html("Ch9_2_3_02.html")