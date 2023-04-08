def inc(x):
  x += 1
  print("Inside function inc")
  print("x =", x)

def dec(x):
  x -= 1
  print("Inside function dec")
  print("x =", x)

x = 100
print("x =", x)
print()

inc(x)
print()

print("Outside function inc")
print("x =", x)
print()

dec(x)
print()

print("Outside function dec")
print("x =", x)


"""
$ python function_arg.py
x = 100

Inside function inc
x = 101

Outside function inc
x = 100

Inside function dec
x = 99

Outside function dec
x = 100
"""
