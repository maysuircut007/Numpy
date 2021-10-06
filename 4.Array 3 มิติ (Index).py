import numpy as np

a = np.array([[[1, 3, 5],[2, 4, 6]],[[7, 8, 9],[10, 11, 12]]])
print(a,"\n",a.ndim)
#a[dept][row][col]
#x = a[0][0][1] # การเข้าถึง index array 3 มิติ
#print(x)
#x = a[0][0][1] + a[-1][1][-2] # การบวก 
#print(x)
#a[0][1][2] = 100
#print(a)