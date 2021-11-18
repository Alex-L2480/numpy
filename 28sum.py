import numpy as np
a = np.arange(1,10).reshape(3,3)
print(a)
b = sum(a)
print(b)
c = np.sum(a[1],axis=0,)
print(c)