import pandas as pd
from numpy.random import randint

df1 = pd.DataFrame(randint(5,10,size=(3,4)),columns=["a","b","c","d"])   #使用 亂數套件建立 Dataframe size= 3*4 並設定 columns
df2 = pd.DataFrame(randint(5,10,size=(2,3)),columns=["b","d","a"])   #使用 亂數套件建立 Dataframe size= 2*3 並設定 columns
print(df1)
print(df2)
df1.to_html("Ch9_4_4a_01.html")
df2.to_html("Ch9_4_4a_02.html")
  
df3 = pd.concat([df1,df2])  #呼叫 concat() 函數 連接兩個物件 df1 df2 (直向連接)
print(df3)
df3.to_html("Ch9_4_4a_03.html")

df4 = pd.concat([df1,df2], ignore_index=True) #呼叫 ignore_index() 忽略索引 這樣才能使索引一致
print(df4) 
df4.to_html("Ch9_4_4a_04.html") 