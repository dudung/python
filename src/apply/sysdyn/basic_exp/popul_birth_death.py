from popul import birth_rate as br
from popul import death_rate as dr

dt = 1
t2 = 4; b = br(t2=t2, dt=dt)
t05 = 2; d = dr(t05=t05, dt=dt)

N1 = 1000
N2 = 1000
N3 = 1000

Niter = 10

print("time\tt2\tt05")
print(f"\t{t2}\t{t05}")
print()

print("coeff\tb\td\tb-d")
print(f"\t{b:.4f}\t{d:.4f}\t{b-d:.4f}")
print()

print("t\tN1\tN2\tN3")
for i in range(Niter):
  t = i*dt
  
  print(t, f"{N1:.2f}", f"{N2:.2f}", f"{N3:.2f}", sep='\t')
  
  dN1 = b * N1 * dt;
  dN2 = -d * N2 * dt;
  dN3 = (b - d) * N3 * dt

  N1 += dN1
  N2 += dN2
  N3 += dN3


"""
$ python
popul_birth_death.py
time    t2      t05
        4       2

coeff   b       d       b-d
        0.1892  0.2929  -0.1037

t       N1      N2      N3
0       1000.00 1000.00 1000.00
1       1189.21 707.11  896.31
2       1414.21 500.00  803.38
3       1681.79 353.55  720.08
4       2000.00 250.00  645.42
5       2378.41 176.78  578.50
6       2828.43 125.00  518.51
7       3363.59 88.39   464.75
8       4000.00 62.50   416.56
9       4756.83 44.19   373.37
"""
