import numpy as np
x = np.array([0,0,0,3,np.inf,np.nan])
print(np.iscomplex(x))#proverka na kompleksnoe chislo
print(np.isreal(x))#realnoe chislo
print(np.isscalar(x))#scalarnyi tip
y = np.array([1,2.3,6,3])
print(np.isscalar(y))