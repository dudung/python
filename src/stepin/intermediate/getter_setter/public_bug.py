import math

class Notation:
  
  def __init__(self, value, unit=""):
    x = value
    sign = (x > 0) - (x < 0)
    if x == 0:
      exp = 0
    else:
      exp = int(math.log10(abs(x)))
    coeff = abs(x / 10**exp)
    
    self.sign = ['-', ' ', '+'][sign + 1]
    self.coeff = coeff
    self.base = "10"
    self.exp = exp
    self.unit = unit
  
  def __str__(self):
    if self.coeff == 0:
      return " 0 " + self.unit
    value = ""
    value += self.sign
    value += f"{self.coeff}"
    if self.exp != 0:
      value += " × 10"
    if (self.exp != 0) and (self.exp != 1):
      value += f"^{self.exp}"
    value += " " + self.unit
    return value

z = Notation(-2035.2, "kg/m^3")
print(z)

z.coeff = 1024
print(z)


"""
$ python public_bug.py
-2.0352 × 10^3 kg/m^3
-1024 × 10^3 kg/m^3
"""
