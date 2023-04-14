class Node:
  def __init__(self, value):
    self.id = id
    self.value = value
    self.next = None
  
  def __str__(self):
    val = ""
    val += f"value={self.value}"
    return val
 