import numpy as np
x = np.arange(20)
print(x)
x[(x >= 9) & (x <= 15)] *= -1
print(x)

