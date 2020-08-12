import matplotlib.pyplot as plt
import numpy as np

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]

plt.barh(index, ratings,color='#13063F', edgecolor="#A6BECF") #bar()為直條圖 barh()
plt.yticks(index, labels) #設置 y軸尺規
plt.xlabel("Usage")
plt.title("Programming Language Usage") 
plt.show()
