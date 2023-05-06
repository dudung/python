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

def count(book):
  prev = count_prev(book)
  next = count_next(book)
  total = 1 + prev + next
  return total, prev, next

b1 = Book("Physics")
b2 = Book("Chemistry")
b3 = Book("Biology")
b4 = Book("Medicine")
b5 = Book("Architecture")
b6 = Book("Sport")

b1.prepend(b2) # b2-b1
b1.append(b3)  # b2-b1-b3
b3.prepend(b4) # b4-b2-b1-b3
b1.prepend(b5) # b5-b4-b2-b1-b3
b1.append(b6)  # b5-b4-b2-b1-b3-b6

print("books: b5-b4-b2-b1-b3-b6")
print("(total, prev, next)")

n = count(b1)
print("using b1:", n)
n = count(b2)
print("using b2:", n)
n = count(b3)
print("using b3:", n)
n = count(b4)
print("using b4:", n)
n = count(b5)
print("using b5:", n)
n = count(b6)
print("using b6:", n)



"""
$ python linked_list.py
books: b5-b4-b2-b1-b3-b6
(total, prev, next)
using b1: (6, 3, 2)
using b2: (6, 2, 3)
using b3: (6, 4, 1)
using b4: (6, 1, 4)
using b5: (6, 0, 5)
using b6: (6, 5, 0)
"""
