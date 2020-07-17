import numpy as np
#EXPLORING NUMPY LIBRARY

#BASIC
veca= np.array([5,10,20])
print(veca)
#Bi-dimensional array
vecb= np.array([[1.0,2.0,3.0,4.0],[1.0,2.0,3.0,4.0]])
print(vecb)
#Get dimension
dimentionb=vecb.ndim
print('Dimension:',dimentionb)
#Get shape
shapeb=vecb.shape
print('Shape:',shapeb)
#Get type
typea=veca.dtype
print('Type:',typea)
#Get items size
items=veca.itemsize
print('Item Size:',items)
#Get size
sizeb=vecb.size
print('Size:',sizeb)
sizea=veca.size
print('Size:',sizea)

#ACCESING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS ETC.
print()
matA= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('New matrix:')
print(matA)
shape=matA.shape
print(shape)
#Get a specific element [rows,columns]
print(matA[1,5])
#Get a specific row
print(matA[0,:])
print(matA[1,:])
#Get a specific column
print(matA[:,2])
print(matA[:,6])
#Getting a little more fancy [starindex, endindex, stepsize]
print(matA[1,0:7:3])
print(matA[1,0:5:1])
print('--')
print(matA[0,1:7:2])

#incomplete
