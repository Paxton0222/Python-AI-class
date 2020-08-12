import matplotlib.pyplot as plt

x = [21,42,23,4,5,26,77,88,9,10,31,32,33,34,35,36,37,18,49,50,100]
#x = [x for i in range(0,10,1)]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins) #hist() 繪製直方圖 hist(index,分割成幾個區間)
print(type(plt.hist(x, num_bins)))
print(n)
print(bins)
print(patches)
plt.show()

