v1 = object()
print("v1 ->",end="")
print(v1)
v2 = v1
print("v2 ->",end="")
print(v2)
v1 = object()
print("v1 ->",end="")
print(v1)
v2 = v1
print("v2 ->",end="")
print(v2)

import gc
gc.collect()

