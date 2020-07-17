import numpy as np 
#Quiz
matrixA=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]])
print(matrixA)
print()
print('Find the following:')
print()
print('1. Size')
print('2. Shape')
print('3. Dimension')
print('4. Even elements')
print('5. Odd elements')
print()
matrixB=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(matrixB)
print()
print('Find the following positions:')
print()
print('6. A3,1  A3,2  A4,1  A4,2')
print('7. A1,2  A2,3  A3,4  A4,5')

print('----------------------------------')
print()
size=matrixA.size
shape=matrixA.shape
dimension=matrixA.ndim
print('SIZE: ',size)
print('SHAPE: ',shape)
print('DIMENSION: ',dimension)
print('EVEN ELEMENTS: ')
for n in range (0,3):
  print(matrixA[n,1:6:2])

print('ODD ELEMENTS: ')
for x in range (0,3):
  print(matrixA[x,0:6:2])

print('POSITIONS: ')
print(matrixB[2:4,0:2])
print()
print(matrixB[[0,1,2,3],[1,2,3,4]])
