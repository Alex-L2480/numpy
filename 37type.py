import numpy as np #чтобы конвертировать ntyp-типы в нативные типы Python. 
print("numpy.float32 to python float")
x = np.float32(1)
print(type(x))
pyval = x.item()
print(type(pyval))
print(pyval)