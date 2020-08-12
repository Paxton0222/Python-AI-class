import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.tail(3))
# 新增記錄
df.loc["third-1"] = ["台北市", "士林區", 288340] #pandas loc()函數可以靠一個不存在的欄位新增一行資料集
print(df.tail(3))
df.tail(3).to_html("Ch9_4_3_01.html")
s = pd.Series({"city":"新北市","name":"中和區","population":413291}) #用字典建立一個新的series陣列物件
df2 = df.append(s, ignore_index=True) #在 df 中加入一個 series 陣列 並且 ignore_index設定為 True
print(df2.tail(3))
df2.tail(3).to_html("Ch9_4_3_02.html")