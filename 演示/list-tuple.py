#有序可變動的列表 list
#可以取得列表中的"元素"(索引)，從0開始算起

grades=[12,60,15,70,90]
print(grades)
print(grades[0]) #取值(0)

grades[0]=55 #把55放到列表中的第一個位置
print(grades)
print(grades[1:4])

grades[1:4]=[] #連續刪除列表中從編號1到編號4(不包括)的資料
print(grades)

grades=grades+[12,33] #原列表加上新的列表做串接
print(grades)

length=len(grades) #len()是列表的長度
print(length)

#列表中的列表
data = [[3,4,5],[6,7,8]]
print(data[0][1])
data[0][0:2]=[5,5,5] #列表0中 從0開始不包含2 故所以保留最後5
print(data)

#有序不可變動的列表 tuple
data=(3,4,5)
#data[0]=5  錯誤:tuple的資料不可調整!
print(data[0:2])


