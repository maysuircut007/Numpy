import numpy as np
a = np.array([[1, 2, 3],[4, 5, 6],[7,8,9]])
print(a[:,:],"\n")
print(a[:2,1:2], "\n")
print(a[1:2,1:2], "\n")
#a[row, column, step]
print(a[:3:2,:], "\n") # หรือ a[::2,:]
print(a[:,:3:2], "\n")  # หรือ a[:,::2]
print(a[1:2,::2]) # หรือ a[1:2,::2] 