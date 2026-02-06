import numpy as np

arr = np.random.randint(100, size=(5,10))

max_value = np.max(arr, axis=1, keepdims=True) 
max_value_idx = np.argmax(arr, axis=1, keepdims=True)
summary = np.column_stack((max_value,max_value_idx))
print(summary)