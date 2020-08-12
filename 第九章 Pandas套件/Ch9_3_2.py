import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[df.population > 350000]) #使用 numpy 布林值索引
df[df.population > 350000].to_html("Ch9_3_2_01.html")

print(df[df["city"].isin(["台北市","高雄市"])]) #透過 isin()函數 查詢指定欄位中是否有鍵入的搜尋值
df[df["city"].isin(["台北市","高雄市"])].to_html("Ch9_3_2_02.html")
