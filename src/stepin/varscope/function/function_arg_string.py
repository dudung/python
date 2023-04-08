def change(s):
  print("Inside function change")
  print(s)
  s = "changed"
  print(s)

s = "original"

print("Before calling function change")
print(s)
print()

change(s)
print()

print("After calling function change")
print(s)


"""
$ python function_arg_string.py
Before calling function change
original

Inside function change
original
changed

After calling function change
original
"""
