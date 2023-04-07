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
