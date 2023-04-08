class Sphere:
  def __init__(self, radius=1):
    self.type = "Sphere"
    self.radius = radius
  
  def __str__(self):
    n = len(self.__dict__.items())
    i = 0
    lines = ""
    for attr, value in self.__dict__.items():
      lines += attr + "=" + str(value)
      if i < n - 1:
        lines += "\n"
      i += 1
    return lines

class SolidSphere(Sphere):
  def __init__(self, radius=1, density=1000):
    Sphere.__init__(self, radius)
    self.type = "SolidSphere"
    self.density = density

s = Sphere()
print(s)
print()

ss = SolidSphere()
print(ss)
