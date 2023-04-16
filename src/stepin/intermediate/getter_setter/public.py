import math

class Param:
  
  def __init__(self, value):
    self.value = value
  
  def __str__(self):
    return str(self.value)

z = Param(10.53)
print(z)

z.value = "-300.1"
print(z)


"""
$ python public.py
10.53
-300.1
"""
