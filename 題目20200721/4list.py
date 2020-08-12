#建立一個串列並且輸入數個不等的資料，利用for迴圈依序的寫出來。
list_= ['123','456','789','apple']
len_ = len(list_)
print(len_)
#ans1
for index in range(len_):
    print(list_[index])
#ans2
for index in list_:
    print(index)