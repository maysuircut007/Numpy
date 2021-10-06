import numpy as np
a = np.array([1,2.3,4,5,6])
b = np.array([7,8,9,10,11,12])
c = np.concatenate((a,b))
#print(c)

# การต่อท้ายแบบ 1 มิติ
"""
a = np.append(a, 500) 
print(a)
"""
# การต่อท้ายแบบ 2 มิติ
d = np.array([[1,2],[4,5]])
e = np.append(d, [[10],[20]], axis = 1)
print(e)
f = np.append(d, [[10,20]], axis = 0)
print(f)

