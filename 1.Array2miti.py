# array มีชนิดข้อมูลเหมือนกัน มีขนาดที่เเน่นอน
# nd array = arlay ที่ถูกสร้างจาก numpy
import numpy as np

a = np.array([1,2,3]) # array 1 มิติ
#print(a, a.ndim) # .ndim => ตรวจสอบมิติของ array
b = np.array([[1, 2, 3],[4 ,5, 6]]) # array 2 มิติ
print(b, b.ndim) 

# array 3 มิติ
a = np.array([[[1, 3, 5],[2, 4, 6]],[[7, 8, 9],[10, 11, 12]]])
print(a,"\n",a.ndim)
