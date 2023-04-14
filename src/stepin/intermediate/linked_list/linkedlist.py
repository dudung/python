class LinkedList:
  def __init__(self):
    self.head = None
    self.n = 0

  def __str__(self):
    val = f"nodes={self.n}"
    return val
  
  def append(self, node):
    self.n += 1
    current = self.head
    if current == None:
      self.head = node
    else:
      while current.next != None:
        current = current.next
      current.next = node
