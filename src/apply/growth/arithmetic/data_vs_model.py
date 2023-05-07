import statistics as s
import matplotlib.pyplot as plt

def diff(x):
  n = len(x)
  d = [(x[i+1] - x[i]) for i in range(n-1)]
  return d

xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ydata = [0, 1.2, 2.5, 3.7, 4.4, 5.1, 5.7, 6.5, 7.8, 9.3, 10]
n = len(ydata)

dy = diff(ydata)
Dy = s.mean(dy)
ymodel = [ydata[0] + i * Dy for i in range(n)]

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
