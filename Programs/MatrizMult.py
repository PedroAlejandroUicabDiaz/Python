mat1=[]
mat2=[]
matr=[]
#We entered the size of matrix 1
print("First Matrix")
fmat1=int(input("Rows: "))
cmat1=int(input("Columns: "))
#We entered the size of matrix 2
print("\nSecond Matrix")
fmat2=int(input("Rows: "))
cmat2=int(input("Columns: "))
#Verification
if cmat1!=fmat2:
  print("Error")
else:
  #We enter the elements of matriz1
  print("\n")
  for z in range(0,fmat1):
    mat1.append([0]*cmat1)
  for i in range(0,fmat1):
    for j in range(0,cmat1):
      mat1[i][j]= int(input("Matrix 1[%d][%d]: "%(i,j)))
  print("\n X \n")
  #We enter the elements of matriz2
  for z in range(0,fmat2):
    mat2.append([0]*cmat2)
  for i in range(0,fmat2):
    for j in range(0,cmat2):
      mat2[i][j]= int(input("Matrix 2[%d][%d]: "%(i,j)))

  #We create the new matrix
  for k in range(0,fmat1):
    matr.append([0]*cmat2)
    for j in range(0,cmat2):
      matr[k][j]=0
  for i in range(0,fmat1):
    for j in range(0,cmat1):
      for k in range(0,cmat2):
        matr[i][k]+= mat1[i][k]*mat2[j][k]
  print("\n = \n")

#We print the result
print("New Matrix\n")
x=""
for i in range(0,fmat1):
  for k in range(0,cmat2):
    x+=str(matr[i][k])+'\t'
  print (x)
  x=""
