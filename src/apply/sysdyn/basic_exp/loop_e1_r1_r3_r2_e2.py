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


"""
$ python loop_e1_r1_r3_r2_e2.py
R1 = 4 E1 = 60
R2 = 2 E2 = 30
R3 = 2

t       I1      V1      I2      V2      I3      V3
0       -3.000, 1.000   -15.000, 3.000  7.000, 0.000
1       15.000, 60.000  9.000, 18.000   24.000, 48.000
2       7.000, 28.000   0.000, 0.000    7.000, 14.000
3       10.000, 40.000  4.000, 8.000    14.000, 28.000
4       8.667, 34.667   2.500, 5.000    11.167, 22.333
5       9.167, 36.667   3.167, 6.333    12.333, 24.667
6       8.944, 35.778   2.917, 5.833    11.861, 23.722
7       9.028, 36.111   3.028, 6.056    12.056, 24.111
8       8.991, 35.963   2.986, 5.972    11.977, 23.954
9       9.005, 36.019   3.005, 6.009    12.009, 24.019
10      8.998, 35.994   2.998, 5.995    11.996, 23.992
11      9.001, 36.003   3.001, 6.002    12.002, 24.003
12      9.000, 35.999   3.000, 5.999    11.999, 23.999
13      9.000, 36.001   3.000, 6.000    12.000, 24.001
14      9.000, 36.000   3.000, 6.000    12.000, 24.000

numerical solution:
I1 = 9.000
I2 = 3.000

Analytical solution:
I1 = 9.0
I2 = 3.0
"""


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
