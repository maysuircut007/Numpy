import numpy as np
x = np.array([[1,2],[3,4]])
y = np.array([[11,12],[13,14]])
z = x.dot(y) # => z =[[1*11+2*13],[3*11+4*13],[1*12+2*14],[3*12+4*14]]
print(z)