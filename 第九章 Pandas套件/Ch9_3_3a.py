import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
df.head().to_html("Ch9_3_3a_01.html")

df2 = df.sort_values("population", ascending=False) #降幕排序
print(df2.head())
df2.head().to_html("Ch9_3_3a_02.html")
#中文排序方式是筆劃排序 inplace=True 時，群組排序會是找一樣的資料進行升幕和降幕排序，可以把 inplace()改成 False 試試
df.sort_values(["city","population"], inplace=True) #群組排序 排序 city 欄位 和 排序 population 欄位為 升幕排序(台北市部分)
print(df.head())
df.head().to_html("Ch9_3_3a_03.html")