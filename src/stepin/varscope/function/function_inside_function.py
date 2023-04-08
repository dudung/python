def outter():
  x = 2

  def inner():
    x = 1
    
    print("Inside function inner")
    print(x)
    print()
  
  print("Inside function outter before calling inner")
  print(x)
  print()
  
  inner()
  print()

  print("Inside function outter affter calling inner")
  print(x)
  print()

x = 3

print("Outside any functions outter before calling outter")
print(x)
print()

outter()
print()

print("Outside any functions outter after calling outter")
print(x)


"""
function_inside_function.py
Outside any functions outter before calling outter
3

Inside function outter before calling inner
2

Inside function inner
1


Inside function outter affter calling inner
2

Outside any functions outter after calling outter
3
"""
