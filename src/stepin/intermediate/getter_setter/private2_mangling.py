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

# it can not be accessed directly
b.__title = "Leveling your Python"
print(b)

# but with this
b._Book__title = "Mastering Python"
print(b)


"""
$ python private2_mangling.py
Learning Python
Learning Python
Mastering Python
"""
