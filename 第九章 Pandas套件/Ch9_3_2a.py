import pandas as pd

df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[(df.population > 350000) & (df.population < 500000)]) #使用範圍搜尋
df[(df.population > 350000) & (df.population < 500000)].to_html("Ch9_3_2a_01.html")

print(df[df["city"].str.startswith("台")]) #搜尋欄位"city"中 第一個字帶有"台"的
df[df["city"].str.startswith("台")].to_html("Ch9_3_2a_02.html")