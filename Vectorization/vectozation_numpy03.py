import numpy as np
from timeit import Timer
#function to select the higher
def python_grader(x,y):
  if x >= y:
    return x
  else:
    return y
#vectorization
numpy_grader=np.vectorize(python_grader,otypes=[int])
#Our arrays
arrA=np.array([2,5,8,13,2])
arrB=np.array([4,2,7,23,4])
#Show the results
print(numpy_grader(arrA,arrB))
#Time
print(min(Timer(numpy_grader).repeat(10, 10)))
