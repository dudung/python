from node import Node

class LinkedList:
  def __init__(self):
    self._head = None
    self._count = 0
  
  @property
  def count(self):
    return self._count
  
  def append(self, data):
    node = self._head
    if node == None:
      nn = Node(data)
      self._head = nn
    else:
      while node.next != None:
        node = node.next
      nn = Node(data)
      node.next = nn
    
    self._count += 1
  
  def list(self):
    value = []
    node = self._head
    while node != None:
      value.append(node.data)
      node = node.next
    return value
  
  def pop(self):
    prev = None
    node = self._head
    
    if node == None:
      return ''
    
    while node.next != None:
      prev = node
      node = node.next
    value = node
    
    if prev != None:
      prev.next = None
    else:
      self._head = None
    self._count -= 1
    
    return value
