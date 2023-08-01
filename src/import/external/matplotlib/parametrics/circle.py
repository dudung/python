import math

T = 1
Nt = 100
dt = T / Nt
omega = 2 * math.pi / T

xc = 1
yc = 3
R = 2
Ax = R
Ay = R
omegax = omega
omegay = omega

phix = 0.5 * math.pi
phiy = 0


t = [i * dt for i in range(Nt+1)]
x = [Ax * math.sin(omegax * i + phix) + xc for i in t]
y = [Ay * math.sin(omegax * i + phiy) + yc for i in t]


import matplotlib.pyplot as plt

plt.plot(x, y, 'r-')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
