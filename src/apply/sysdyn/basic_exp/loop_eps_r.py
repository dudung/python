R = 2.5
eps = 10
I = 2
V = 5
print("eps =", eps)
print("R =", R)
print()

print("t\tI\tV")
for t in range(10):
  print(t, I, V, sep='\t')
  
  dI = (eps - V) / R
  dV = R * dI
  
  V = V + dV
  I = I + dI
