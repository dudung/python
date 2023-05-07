import statistics as s
import matplotlib.pyplot as plt

def ratio(x):
  n = len(x)
  d = [(x[i+1] / x[i]) for i in range(n-1)]
  return d

xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ydata = [2, 4, 10, 16, 32, 60, 100, 250, 500, 1000, 2100]
n = len(ydata)

gamma = ratio(ydata)
c = s.mean(gamma)
ymodel = [ydata[0] * c**i for i in range(n)]

print("x", "ydata", "ymodel", sep='\t')
for i in range(n):
  print(xdata[i], end='\t')
  print(ydata[i], end='\t')
  print(ymodel[i])

plt.plot(xdata, ydata, 'ro:', xdata, ymodel, 'b-')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend(["data", "model"])
plt.show()
