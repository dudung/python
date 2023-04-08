class First:
  def __init__(self):
    print("Initialize instance")
    
    print(x)
    
    self.x = 100
    print(self.x)

x = 2

print("Before creating instance of class First")
print(x)
print()

f = First()
print()

print("After creating instance of class First")
print(x)
print()


print("Call instance attribute")
print(f.x)


"""
$ python global_var_in_class.py
Before creating instance of class First
2

Initialize instance
2
100

After creating instance of class First
2

Call instance attribute
100
"""
