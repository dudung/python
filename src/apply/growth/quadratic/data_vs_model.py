import statistics as s
import matplotlib.pyplot as plt

def diff(x):
  n = len(x)
  d = [(x[i+1] - x[i]) for i in range(n-1)]
  return d

xdata = [0, 1, 2,  3,  4,  5,  6,  7,  8,  9,  10]
ydata = [0, 1, 5, 11, 19, 30, 42, 60, 70, 87, 108]
n = len(ydata)

dy = diff(ydata)
Dy = dy[0]
ddy = diff(dy)
DDy = s.mean(ddy)
ymodel = [ydata[0] + i*Dy + 0.5*(i)*(i-1)*DDy for i in range(n)]

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
