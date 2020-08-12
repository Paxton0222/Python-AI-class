import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.loc[ordinals[1]]) #使用索引搜尋器搜尋資料
print(type(df.loc[ordinals[1]]))
print(df.loc[:,["name","population"]].head(3)) #使用二維陣列的方式去抓取資料 loc(index,data)
df.loc[:,["name","population"]].head(3).to_html("Ch9_3_1b_01.html") #存檔
print('---------------------------------')
print(df.loc["third":"fifth", ["name","population"]]) #使用二維陣列的方式去抓取資料 loc(index,data)
print(df.loc["third", ["name","population"]]) #使用二維陣列的方式去抓取資料 loc(index,data)
df.loc["third":"fifth", ["name","population"]].to_html("Ch9_3_1b_02.html") #存檔
# 取得單一純量值
print('---------------------------------')
print(df.loc[ordinals[0], "name"]) #搜尋索引值 0 的 "name"
print(type(df.loc[ordinals[0],"name"])) #資料型態
print(df.loc["first", "population"]) #索引值 first 的 "population"
print(type(df.loc["first", "population"])) #資料型態
