import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")

for index, row in df.iterrows() : #使用 iterrows() 函數走訪每個資料
    print(index, row["city"], row["name"], row["population"])