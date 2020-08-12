import matplotlib.pyplot as plt

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
explode = (0, 0, 0, 0.2, 0, 0.2)#指定突出增值

plt.pie(ratings, 
        labels=labels,
        explode=explode) 
plt.title("Programming Language Usage") 
plt.axis("equal")
plt.show()
