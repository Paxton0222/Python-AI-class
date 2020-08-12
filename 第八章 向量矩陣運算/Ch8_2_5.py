import numpy as np

a = np.arange(10) #創建 0-9 的一維陣列
outputfile = "Example.npy" 
with open(outputfile, 'wb') as fp: #使用二進制寫入檔案
    np.save(fp, a) #np.save(file,array)
