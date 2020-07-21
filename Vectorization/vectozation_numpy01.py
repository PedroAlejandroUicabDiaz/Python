import numpy as np 
import time 
#Matriz multiplication 
#We create our vectors
size=1000
np.random.seed(0)
vectA=np.random.random(size)
vectB=np.random.random(size)

#We make the code as we are used to 
#To see which was faster, we create a variable that takes time
Time=time.process_time()
multiplication=np.zeros((size,size))
#For-Loop
for i in range(size):
  for j in range(size):
    multiplication[i][j]=vectA[i]*vectB[j]

#Time spent doing the operation
python_time=time.process_time() - Time
#Vectorization 
Time= time.process_time()
np_multiplication=np.outer(vectA,vectB)
#Time spent doing the operation
numpy_time=time.process_time() - Time
#Results
print('Python Time:',python_time)
print('Numpy Time:',numpy_time)
"""
Links:
https://realpython.com/numpy-array-programming/
https://towardsdatascience.com/data-science-with-python-turn-your-conditional-loops-to-numpy-vectors-9484ff9c622e
https://www.analyticslane.com/2020/05/25/vectorizacion-en-python-para-mejorar-el-rendimiento/
"""
