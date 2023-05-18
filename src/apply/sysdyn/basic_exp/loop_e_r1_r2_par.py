eps = 12
R1 = 1.5
R2 = 6

V1 = -194
V2 = -353
I1 = 50
I2 = -20

print("eps =", eps)
print("R1 =", R1)
print("R1 =", R2)
print()

print("t\tI1\tV1\tI2\tV2")
for t in range(10):
  print(t, I1, V1, I2, V2, sep='\t')
  
  if abs(V1 - V2) < 1E-10:
    print("Solved in", t, "iteration")
    break
  
  dI1 =  (eps/R1) - (1/R1) * V1
  I1 = I1 + dI1

  dI2 =  (eps/R2) - (1/R2) * V2
  I2 = I2 + dI2
  
  V1 = R1 * I1
  V2 = R2 * I2
