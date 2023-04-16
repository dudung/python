import math

class Thing:
  
  def __init__(self, mass=1, volume=1):
    self.mass = mass
    self.volume = volume
    self.density = mass / volume
  
  def __str__(self):
    value = ""
    value += f"mass = {self.mass}\n"
    value += f"volume = {self.volume}\n"
    value += f"density = {self.density}"
    return value

z = Thing(2.5, 0.5)
print(z)

print()

z.mass = 2
z.volume = 4
print(z)


"""
$ python public_bug.py
mass = 2.5
volume = 0.5
density = 5.0

mass = 2
volume = 4
density = 5.0
"""
