class Book:
  def __init__(self, title):
    self.title = title
    self.next = None
    self.prev = None
  
  def append(self, book):
    if self.next == None:
      self.next = book
      book.prev = self
    else:
      last = self.next
      while last.next != None:
        last = last.next
      last.next = book
      book.prev = last
  
  def prepend(self, book):
    if self.prev == None:
      self.prev = book
      book.next = self
    else:
      first = self.prev
      while first.prev != None:
        first = first.prev
      first.prev = book
      book.next = first

def count_next(book):
  if book.next == None:
    return 0
  else:
    return 1 + count_next(book.next)

def count_prev(book):
  if book.prev == None:
    return 0
  else:
    return 1 + count_prev(book.prev)


b1 = Book("Physics")
b2 = Book("Chemistry")
b3 = Book("Biology")
b4 = Book("Medicine")
b5 = Book("Architecture")
b6 = Book("Sport")

b1.prepend(b2)
b1.append(b3)
b3.prepend(b4)
b1.prepend(b5)
b1.prepend(b6)




print(count_next(b1))
print(count_prev(b1))