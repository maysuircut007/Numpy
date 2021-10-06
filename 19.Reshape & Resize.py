import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])

# reshape
b = a.reshape(2, 5) # reshape ต้องเก็บค่าในตัวแปลใหม่
print(b)
a.resize(2, 5) # resize ไม่ต้องเก็บค่าในตัวเเปลใหม่
print(a)