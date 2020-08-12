import numpy as np

a = np.array([1,2,3,4,5,6])
print("a=" + str(a))

b = np.reshape(a,(3,2)) #重建陣列形狀維為 3*2
print("b=np.reshape(a,(3,2))->")
print(b)
c = b.T #交換陣列維度 2*3
print("c=b.T->")
print(c)
c = b.transpose() #交換陣列維度 2*3
print("c=b.transpose()->")
print(c)
c = np.transpose(b) #不同寫法
print("c=np.transpose(b)->")
print(c)