from time import perf_counter as pc
t0 = pc()

from person import Person

persons = []
persons.append(Person(name="Amir", age=14, weight=40))
persons.append(Person(weight=42, name="Budi", age=16))
persons.append(Person(age=15, weight=38, name="Wati"))

for i in persons:
  print(i)

print(pc()-t0)
# 0.007803000000421889 s
# 224 bytes -- without pc
