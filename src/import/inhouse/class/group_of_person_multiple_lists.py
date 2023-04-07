from time import perf_counter as pc
t0 = pc()

names = ["Amir", "Budi", "Wati"]
ages = [14, 16, 15]
weights = [40, 42, 38]

n = len(names)

for i in range(0, n):
  print("Name   :", names[i])
  print("Age    :", ages[i])
  print("Weight :", weights[i])
  print()

print(pc()-t0)
# 0.010093100005178712 s
# 227 bytes -- without pc
