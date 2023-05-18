eps = 12
R1 = 1.5
R2 = 2.5

I = -360
V1 = 10
V2 = -20

print("eps =", eps)
print("R1 =", R1)
print("R1 =", R2)
print()

Inew = I + 100
print("t\tI\tV1\tV2")
for t in range(10):
  print(t, I, V1, V2, sep='\t')
  
  dI =  (eps/(R1 + R2))
  dI += -(1/(R1 + R2)) * V1
  dI += -(1/(R1 + R2)) * V2
  I = I + dI
  
  V1 = R1 * I
  V2 = R2 * I
  
  if abs(Inew - I) < 1E-10:
    print()
    print("Solved in", t, "iteration")
    break
  else:
    Inew = I

"""
$ python loop_e_r1_r2_ser.py
eps = 12
R1 = 1.5
R1 = 2.5

t       I       V1      V2
0       -360    10      -20
1       -354.5  -531.75 -886.25
2       3.0     4.5     7.5

Solved in 2 iteration
"""
