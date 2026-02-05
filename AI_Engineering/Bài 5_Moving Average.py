import numpy as np

# Bài 5_Moving Average
np.set_printoptions(formatter={'float': '{:0.2f}'.format}) # in ra đẹp hơn
Revenue_per_day = np.random.randint(1, 101, size=10) 
res = np.convolve(Revenue_per_day, np.ones(3) / 3 , 'valid')
print(res)