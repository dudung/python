def solution(E1=1, R1=1, E2=1, R2=1, R3=1):
  denom = (R1 + R3) * (R2 + R3) - R3 * R3
  nom1 = R2 + R3
  nom2 = R1 + R3
  I1 = ( nom1 * E1 +  -R3 * E2) / denom
  I2 = ( -R3  * E1 + nom2 * E2) / denom
  return I1, I2

# define parameters
R1 = 4; E1 = 60
R2 = 2; E2 = 30
R3 = 2
print("R1 =", R1, "E1 =", E1)
print("R2 =", R2, "E2 =", E2)
print("R3 =", R3)
print()

# initial condition
I1 = -3
I2 = -15
I3 = 7
V1 = 1
V2 = 3
V3 = 0

# show iteration
print("t\tI1\tV1\tI2\tV2\tI3\tV3")
Nt = 15
for t in range(Nt):
  if True:
    pass  
  
  print(
    t,
    f"{I1:.3f}, {V1:.3f}",
    f"{I2:.3f}, {V2:.3f}",
    f"{I3:.3f}, {V3:.3f}",
    sep='\t'
  )
  
  dI1 = (E1 - I2 * R3) / (R1 + R3) - I1
  dI2 = (E2 - I1 * R3) / (R2 + R3) - I2
  
  I1 = I1 + dI1
  I2 = I2 + dI2
  I3 = I1 + I2
  
  V1 = I1 * R1
  V2 = I2 * R2
  V3 = I3 * R3
print()

# numerical solution
print("numerical solution:")
print(f"I1 = {I1:.3f}")
print(f"I2 = {I2:.3f}")
print()

# analytical solution
I1, I2 = solution(E1=E1, R1=R1, E2=E2, R2=R2, R3=R3)
print("Analytical solution:")
print("I1 =", I1)
print("I2 =", I2)


# schematic diagram
"""
         R1        R2
    +--/\/\/--+--/\/\/--+
    |         |         |
    |         X         |
E1 --- +      X R3  E2 --- +
    -         X         -
    | <-- I1  | I2 -->  |
    +---------+---------+
"""

# Kirchhof 1st rule
"""
E1 - I1 * R1 - I3 * R3 = 0
E2 - I2 * R1 - I3 * R3 = 0
E1 - I1 * R1 + I2 * R2 - E2 = 0
"""

# Kirchhof 2nd rule
"""
I3 - I1 - I2 = 0
"""

# Ohm's law
"""
V1 = I1 * R1
V2 = I2 * R2
V3 = I3 * R3
"""

#I1
"""
E1 = I1 * (R1 + R3) + I2 * R3
E2 = I1 * R3        + I2 * (R2 + R3)

E1 * (R2 + R3) = I1 * (R1 + R3) * (R2 + R3) + I2 * R3 * (R2 + R3)
E2 * R3        = I1 * R3 * R3               + I2 * R3 * (R2 + R3) 

E1 * (R2 + R3) - E2 * R3 = I1 * ((R1 + R3) * (R2 + R3) - R3 * R3)
I1 = (E1 * (R2 + R3) - E2 * R3) / ((R1 + R3) * (R2 + R3) - R3 * R3)
"""

# I2
"""
E2 = I1 * R3        + I2 * (R2 + R3)
E1 = I1 * (R1 + R3) + I2 * R3

E2 * (R1 + R3) = I1 * (R1 + R3) * R3 + I2 * (R1 + R3) * (R2 + R3)
E1 * R3        = I1 * (R1 + R3) * R3 + I2 * R3 * R3

E2 * (R1 + R3) - E1 * R3 = I2 * ((R1 + R3) * (R2 + R3) - R3 * R3)
I2 = (E2 * (R1 + R3) - E1 * R3) / ((R1 + R3) * (R2 + R3) - R3 * R3)
"""
