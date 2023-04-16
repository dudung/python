class Id4d:
  def __init__(self, id):
    self._value = f"{id:04d}"
  
  def __str__(self):
    return str(self._value)
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, id):
    self._value = f"{id:04d}"

id = Id4d(1)
print(id)

id.value = 83
print(id)

# but do not do this
id._value = 361
print(id)


"""
$ python id4d_property.py
0001
0083
361
"""
