import numpy as np
#讀取剛剛用2進制寫入的檔案
outputfile = "Example.npy"
with open(outputfile, 'rb') as fp:
    a = np.load(fp) #使用np.load()函數
print(a)