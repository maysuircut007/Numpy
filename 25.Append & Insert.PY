import numpy as np
a = np.array([1,2,3,4,8])
b = np.append(a, 40)
print(b)

c = np.insert(a, 1, 100)
print(c)

d = np.insert(a, (1,3), 100)
print(d) 
