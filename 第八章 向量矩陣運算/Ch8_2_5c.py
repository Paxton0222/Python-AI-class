import numpy as np
#讀取剛剛存入的.out檔案中的陣列
outputfile = "Example.out"
a = np.loadtxt(outputfile, delimiter=',')
print(a)
