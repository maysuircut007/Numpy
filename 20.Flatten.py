import numpy as np

a = np.array([[1,2],[3,4],[5,6]])

# .flatten()
b = a.flatten() # แปลง 2 มิติเป็น 1 มิติ
print(b)
b[0] = 5 # .flatten() เมื่อเปลียนข้อมูลใน b ไม่เปลียนข้อมูลใน a ด้วย
print(b)
print(a)

# .ravel()
c = a.ravel()
print(c)
c[0] = 5 # .ravel() เมื่อเปลียนข้อมูลใน c ก็จะเปลียนข้อมูลใน a ด้วย
print(b)
print(a)