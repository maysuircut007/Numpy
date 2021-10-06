import numpy as np
a = np.array([1, 2, 3, 4, 5, 6,])
print(a.sum()) 
print(a.prod())
print(a.max())
print(a.min())
print(a.mean())
print(a.argmax())  # index ที่ข้อมูลค่ามากที่สุด
print(a.argmin())  # index ที่ข้อมูลค่าน้อยที่สุด

x = np.array([[10,30,40],[100,88,50],[77,43,42]])
print(np.min(x,axis = 1)) # axis = 1 คือเเนวนอน
print(np.min(x, axis = 0)) # axis = 0 คือเเนวตั้ง
print(np.max(x,axis = 1)) # axis = 1 คือเเนวนอน
print(np.max(x, axis = 0)) # axis = 0 คือเเนวตั้ง
