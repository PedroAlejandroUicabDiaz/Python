import numpy as np
from timeit import Timer
#We create an array
li = list(range(500))
#The same but with np
nump_arr = np.array(li)
#Function to do the sum
def python_for():
    return [num + 1 for num in li]
#Function to do the sum
def numpy():
    return nump_arr + 1
#Results
print(min(Timer(python_for).repeat(10, 10)))
print(min(Timer(numpy).repeat(10, 10)))

"""
https://realpython.com/numpy-array-programming/
https://www.it-swarm.dev/es/python/que-es-la-vectorizacion/834957754/
"""
