import numpy as np
m = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 1, 0])
print(v)
print(m)
result = np.empty_like(m) #pustoy
for i in range(4):
  result[i, :] = m[i, :] + v
print(result)