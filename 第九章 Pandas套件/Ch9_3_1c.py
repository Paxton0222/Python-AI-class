import pandas as pd
# pandas 切割索引器 iloc()
df = pd.read_csv("dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.iloc[3])          # 第 4 筆 會往後找一筆 因為是從 0 開始
print('---------------------------------')
print(df.iloc[3:5, 1:3])   # 切割 找到"索引值"第四和第五個 並且搜索"欄位"第二和第三個
print('---------------------------------')
print(df.iloc[1:3, :])     # 切割列 找到索引值第二和第三個
print('---------------------------------')
print(df.iloc[:, 1:3])     # 切割欄 找尋所有索引值 並且找到"欄位"二和第三個
print('---------------------------------')
df.iloc[3:5, 1:3].to_html("Ch9_3_1c_01.html")
df.iloc[1:3, :].to_html("Ch9_3_1c_02.html")
df.iloc[:, 1:3].to_html("Ch9_3_1c_03.html")
print('---------------------------------')
print(df.iloc[[1,2,4], [0,2]])   # 索引清單 1,2,4 並且找出"欄位"0,2的資料
df.iloc[[1,2,4], [0,2]].to_html("Ch9_3_1c_04.html")
# 取得單一純量值
print('---------------------------------')
print(df.iloc[1,1]) #切割索引器
print('---------------------------------')
print(df.iat[1,1]) #索引器選擇純量值
