import pandas as pd

df1 = pd.DataFrame({"key":["a","b","b"],"data1":range(3)}) #建立一個 Dataframe
df2 = pd.DataFrame({"key":["a","b","c"],"data2":range(3)}) #建立一個 Dataframes
print(df1)
print(df2)
df1.to_html("Ch9_4_4b_01.html")
df2.to_html("Ch9_4_4b_02.html")
print('df3')
df3 = pd.merge(df1, df2) #呼叫 merge()函式 連接兩個物件 df1 df2 (橫向連接) 預設 key 合併
#因為 df1 沒有 c 欄位值 所以 會忽略掉 c ， 不受順序影響
print(df3)
df3.to_html("Ch9_4_4b_03.html")
print('df4')
df4 = pd.merge(df2, df1)
print(df4)
df4.to_html("Ch9_4_4b_04.html")
#如果想要不忽略掉 c 的話 只需要加上屬性 how 即可 
#left 為左外部合併，right 為右外部合併，outer 為全外部合併
df5 = pd.merge(df2, df1, how='left')
print(df5)
df5.to_html("Ch9_4_4b_05.html")