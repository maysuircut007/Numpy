import numpy as np


a = np.arange(1, 5)
"""
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a**2)
print(a % 2)
"""

b = np.arange(1, 5)
c = np.arange(6, 10)
#print(b + c) # a กับ c ต้องมีขนาดที่เท่ากัน

# ตัวดำเนินการทางคณิตศาสตร์ array 2 มิติ

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6]])
"""
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x**y)
print(x % y)
"""
#print(x + [2])

z = np.array([1,2,3]) 
print(x + z) # array 1 มิติบวกกับ 2 มิติได้หากมีสมาชิกในเเถวเท่ากัน
