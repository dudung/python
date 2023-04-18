import sys
sys.path.append("../")

from linked_list_v2.node import Node

class LinkedList:
  def __init__(self):
    self._head = None
    self._count = 0
  
  @property
  def count(self):
    return self._count
  
  def append(self, value):
    node = self._head
    if node == None:
      nn = Node(value)
      self._head = nn
    else:
      while node.next != None:
        node = node.next
      nn = Node(value)
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
  
  def index(self, value):
    node = self._head
    i = 0
    
    while node.data != value:
      node = node.next
      i += 1
    return i

  def find(self, value):
    node = self._head
    
    while node != None:
      if node.data == value:
        return node
      node = node.next
  
  def prepend(self, value):
    node = self._head
    nn = Node(value)
    self._head = nn
    if node != None:
      self._head.next = node
    self._count += 1
  
  def insert(self, index, value):
    node = self._head
    if node == None or index >= self.count:
      self.append(value)
    elif index == 0:
      self.prepend(value)
    else:
      i = 1
      while i <= index:
        if i == index:
          nn = Node(value)
          next = node.next
          node.next = nn
          nn.next = next
        node = node.next
        i += 1
    self._count += 1
