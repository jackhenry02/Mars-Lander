print("hello")
import numpy as np

dt_array = np.arange(0, 2.1, 0.1)   #Verlet method breaks down using values of dt>1, 100 times higher than Euler

for i in range(len(dt_array)):
    print(dt_array[i])

