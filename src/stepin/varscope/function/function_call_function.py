def f1():
  x = 1
  print("Inside function f1 before calling f2")
  print(x)
  print()
  
  f2()
  print()

  print("Inside function f1 after calling f2")
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


"""
$ python function_call_function.py
Before calling any functions
0

Inside function f1 before calling f2
1

Inside function f2
2

Inside function f1 after calling f2
1

After calling function f1
0
"""
