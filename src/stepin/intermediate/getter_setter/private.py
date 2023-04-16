class Book:
  def __init__(self, title):
    self._title = title
  
  def __str__(self):
    return(self._title)
  
  def set_title(self, title):
    self._title = title

  def get_title(self):
    return self._title


b = Book("Learning Python")
print(b)

b.set_title("Mastering Python")
print(b)


"""
$ python private.py
Learning Python
Mastering Python
"""
