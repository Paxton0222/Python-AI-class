import matplotlib.pyplot as plt
import numpy as np

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]

plt.bar(index, ratings) #bar(x=6,y=6)
plt.xticks(index, labels) #顯示 x軸尺規 index是索引長度 , labels是對應索引的清單
plt.ylabel("Usage")
plt.title("Programming Language Usage") 
plt.show()
