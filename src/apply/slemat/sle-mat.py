x = [i for i in range(0, 11)]
#print(x)
y = [1, -5, -15, -23, -23, -9, 25, 85, 177, 307, 481]
#print(y)

def elema(p, q, x, y):
  sum = 0
  for xi in x:
    sum += xi**(p+q-2)
  return sum
#print(elema(1, 2, x, y))

def elemb(p, q, x, y):
  sum = 0
  for i in range(len(x)):
    sum += y[i] * x[i]**(p+q-2)
  return sum
#print(elemb(1, 1, x, y))
#print(sum(y))

def matrixA(M, x, y):
  mat = []
  for p in range(M+1):
    row = []
    for q in range(M+1):
      # Python list begins form 0
      apq = elema(p+1, q+1, x, y)
      row.append(apq)
    mat.append(row)
  return mat

def matrixB(M, x, y):
  mat = []
  for p in range(M+1):
    bpq = elemb(p+1, 1, x, y)
    mat.append(bpq)
  return mat

def printMatrix(mat):
  for row in mat:
    print(row)

M = 3
matA = matrixA(M, x, y)
#printMatrix(matA)

matB = matrixB(M, x, y)
#printMatrix(matB)
#print(sum(y))

# create Numpy array
import numpy as np
npA = np.array(matA)
npB = np.array(matB)

C = np.linalg.solve(npA, npB)
#print(C)

xx = [i*0.1 for i in range(101)]
def ymodel(xx, C):
  yy = []
  for x in xx:
    sum = 0 
    for j in range(len(C)):
      sum += C[j] * x**j
    yy.append(sum)
  return yy

yy = ymodel(xx, C)
#print(yy)

import matplotlib.pyplot as plt

plt.plot(xx, yy, 'r.')
plt.plot(x, y, 'bo')
plt.show()


