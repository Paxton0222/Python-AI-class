import numpy as np
#使用np.savtxt(file,array,delimiter) 並存入副檔名為 .out 的檔案中
a = np.array([[1,2,3],[4,5,6]])
outputfile = "Example.out"
np.savetxt(outputfile, a, delimiter=',') #插入分隔符號
