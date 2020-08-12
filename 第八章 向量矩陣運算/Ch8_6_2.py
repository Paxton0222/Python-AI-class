import numpy as np

np.random.seed(293423) #提供亂數種子

v1 = np.random.random() #產生0.0-1.0之間的亂數
v2 = np.random.random()
print(v1, v2)
v3 = np.random.randint(5, 10) #產生5-10之間的亂數
v4 = np.random.randint(1, 101) #產生1-100之間的亂數
print(v3, v4)