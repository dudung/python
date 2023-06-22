# import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# create element of A matrix
def elemA(p, q, x, y):
  sum = 0
  for xi in x:
    sum += xi**(p+q-2)
  return sum

# create element of B matrix
def elemB(p, q, x, y):
  sum = 0
  for i in range(len(x)):
    sum += y[i] * x[i]**(p+q-2)
  return sum

# create A matrix
def matrixA(M, x, y):
  mat = []
  for p in range(M+1):
    row = []
    for q in range(M+1):
      # Python list begins form 0
      apq = elemA(p+1, q+1, x, y)
      row.append(apq)
    mat.append(row)
  return mat

# create B matrix
def matrixB(M, x, y):
  mat = []
  for p in range(M+1):
    bpq = elemB(p+1, 1, x, y)
    mat.append(bpq)
  return mat

# print matrix or list of list
def printMatrix(mat):
  for row in mat:
    print(row)

# create predicted values using polynomial function
def ypoly(xx, C):
  yy = []
  for x in xx:
    sum = 0 
    for j in range(len(C)):
      sum += C[j] * x**j
    yy.append(sum)
  return yy

# create data
x = [i for i in range(0, 11)]
y = [1, -5, -15, -23, -23, -9, 25, 85, 177, 307, 481]

# set order of polynomial function as model
M = 3

# create A and B matrices
matA = matrixA(M, x, y)
matB = matrixB(M, x, y)

# create Numpy array
npA = np.array(matA)
npB = np.array(matB)

# solve equation AC = B
C = np.linalg.solve(npA, npB)

# display result
print("C = ", C)

# create from model, more dense than from observation
xx = [i*0.2 for i in range(51)]
yy = ypoly(xx, C)

# plot data from observation
plt.plot(xx, yy, 'r.-')

# plot data from model
plt.plot(x, y, 'bo')

# display result
plt.show()
