class Something:
  def __init__(self, x):
    self.x = x

def change(s):
  print("Inside function change")
  print(s.x)
  s.x = 100
  print(s.x)

s = Something(1)

print("Before calling function change")
print(s.x)
print()

change(s)
print()

print("After calling function change")
print(s.x)


"""
$ python function_arg_object.py
Before calling function change
1

Inside function change
1
100

After calling function change
100
"""
