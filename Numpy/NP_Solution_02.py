#create two matrices where the size is entered by the user, the elements of each matrix will be placed randomly and then perform the multiplication.

import numpy as np

def ask_for_values():
  r=int(input("Rows: "))
  c=int(input("Columns: "))
  #print('[',r,',',c,']')
  create_matrix(r,c)

def create_matrix(r,c):
  matA=np.random.randint(10,size=(r,c))
  print(matA)
  print()
  matB=np.random.randint(20,size=(r,c))
  print(matB)
  mult_matrix(matA,matB)

def mult_matrix(matA,matB):
  m=np.matmul(matA,matB)
  print('---')
  print(m)

ask_for_values()
