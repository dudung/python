class Greeting:
  msg = "Hello"

g = Greeting()

class Reply:
  msg = "Hai"

r = Reply()

print(type(g))
print(type(g).__name__)
print(type(r))
print(type(r).__name__)


"""
<class '__main__.Greeting'>
Greeting
<class '__main__.Reply'>
Reply
"""
