import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
dex = np.array([2,4,6,8])
#print(x[dex])
#print(x[[2,4,6,8]])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(b[[0,2]])
#print(b[[0,2],[2,0]])
#print(b[[0,2],[2]])
m = x[[1,4,1,4,1,4,1,4]]
#print(m)
#rint(x[x>3])
#print(b[b>4])
#print(b[b<4])
n = b[b<3] * 4
print(n)