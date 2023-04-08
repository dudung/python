def change(s):
  print("Inside function change")
  print(s)
  s.append(100)
  print(s)

s = [1]

print("Before calling function change")
print(s)
print()

change(s)
print()

print("After calling function change")
print(s)


"""
$ python function_arg_list.py
Before calling function change
[1]

Inside function change
[1]
[1, 100]

After calling function change
[1, 100]
"""
