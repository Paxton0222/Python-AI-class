import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

df.columns = ["直轄市", "區", "人口"]
print(df.index) #寫出索引
print(df.columns) #寫出 欄位
print(df.values)  #寫出資料