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
  
  def graphs(self):
    val = ""
    current = self.head
    while current != None:
      val += str(current.value)
      current = current.next
      if current != None:
        val += " --> "
    return val
  
  def remove(self, i):
    if self.n == 0 or self.n <= i:
      return
    
    m = 0
    current = self.head
    while current != None:
      if m == i-1:
        next = current.next
        next2 = current.next.next
        current.next = next2
        next.next = None
        break
      current = current.next
      m += 1
    pass
    