class Id4d:
  def __init__(self, id):
    self._value = f"{id:04d}"
  
  def __str__(self):
    return str(self._value)
    
  def change_id(self, id):
    self._value = f"{id:04d}"

id = Id4d(25)
print(id)

id.change_id(873)
print(id)

id._value = 53
print(id)


"""
$ python id4d.py
0025
0873
53
"""
