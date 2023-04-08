def do_something():
  print("Inside function")
  # print(" ", x)
  # UnboundLocalError: local variable 'x' referenced before assignment
  x = 3
  print(x)
  

x = 100

print("Before calling function")
print(x)
print()

do_something()
print()

print("After calling function")
print(x)


"""
$ python one_function.py
Before calling function
100

Inside function
3

After calling function
100
"""
