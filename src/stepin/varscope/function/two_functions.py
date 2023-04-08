def f1():
  x = 1
  print("Inside function f1")
  print(x)

def f2():
  x = 2
  print("Inside function f2")
  print(x)

x = 0

print("Before calling any functions")
print(x)
print()

f1()
print()

print("After calling function f1")
print(x)
print()

f2()
print()

print("After calling function f2")
print(x)


"""
$ python two_functions.py
Before calling any functions
0

Inside function f1
1

After calling function f1
0

Inside function f2
2

After calling function f2
0
"""
