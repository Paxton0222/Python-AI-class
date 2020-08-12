import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
            "sixth", "seventh", "eigth", "ninth", "tenth",
            "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals
#使用 drop() 函數來刪除紀錄
print(df.head())
# 刪除記錄
df2 = df.drop(["second", "fourth"])    # 刪除 2,4 筆
print(df2.head())
df2.head().to_html("Ch9_4_2a_01.html")
df.drop(df.index[[2,3]], inplace=True) # 刪除 3,4 筆
print(df.head())
df.head().to_html("Ch9_4_2a_02.html")