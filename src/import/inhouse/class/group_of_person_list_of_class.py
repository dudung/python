from time import perf_counter as pc
t0 = pc()

# Person class
class Person:
  
  # constructor
  def __init__(self, name="Unknown", age="0", weight="0"):
    self.name = name
    self.age = age
    self.weight = weight
  
  # string representation
  def __str__(self):
    vals = ""
    vals += f"Name   : {self.name}\n"
    vals += f"Age    : {self.age}\n"
    vals += f"Weight : {self.weight}\n"
    return vals

persons = []
persons.append(Person("Amir", 14, 40))
persons.append(Person("Budi", 16, 42))
persons.append(Person("Wati", 15, 38))

for i in persons:
  print(i)

print(pc()-t0)
# 0.006331800002953969 s
# 552 bytes -- without pc
