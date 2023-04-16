class Node:
  def __init__(self, value):
    self._data = value
    self._next = None
  
  def __str__(self):
    return str(self._data)
  
  @property
  def data(self):
    return self._data
  
  @data.setter
  def data(self, value):
    self._data = value
  
  @property
  def next(self):
    return self._next
  
  @next.setter
  def next(self, node):
    self._next = node
