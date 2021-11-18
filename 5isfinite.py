import numpy as np
x = np.array([0,0,0,3,np.inf,np.nan])
print(np.isinf(x))
print(np.isfinite(x))#proverka na konechnost elementov true/false 
