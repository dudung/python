eps = 16
R = 4

I = -12.34
V = 500.005

print("eps =", eps)
print("R =", R)
print()

Vnew = V + 100
print("t\tI\tV")
for t in range(5):
  print(t, I, V, sep='\t')
  
  dI =  -(1/R) * V + (eps/R)
  I = I + dI
  
  V = R * I
  
  if abs(Vnew - V) < 1E-5:
    print()
    print("Solved in", t, "iteration")
    break
  else:
    Vnew = V


"""
$ python loop_e_r.py
eps = 16
R = 4

t       I       V
0       -12.34  500.005
1       -133.34125      -533.365
2       4.0     16.0

Solved in 2 iteration
"""
