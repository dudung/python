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
persons.append(Person(name="Amir", age=14, weight=40))
persons.append(Person(weight=42, name="Budi", age=16))
persons.append(Person(age=15, weight=38, name="Wati"))

for i in persons:
  print(i)

print(pc()-t0)
# 0.005884500002139248 s
# 600 bytes -- without pc
