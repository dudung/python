class Book:
  def __init__(self, title):
    self.__title = title
  
  def __str__(self):
    return(self.__title)
  
  def set_title(self, title):
    self.__title = title

  def get_title(self):
    return self.__title


b = Book("Learning Python")
print(b)

b.set_title("Mastering Python")
print(b)


"""
$ python private2.py
Learning Python
Mastering Python
"""
