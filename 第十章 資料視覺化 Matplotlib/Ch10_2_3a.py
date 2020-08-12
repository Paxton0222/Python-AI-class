import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000) 
num_bins = 50 #取50個區間
plt.hist(x, num_bins) #hist(value,區間)
plt.show()