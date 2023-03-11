print(type([1, 5.93, True, "Hello"]))

x = [1, 5.93, True, "Hello", [1, 5.93, True, "Hello"]]
print(type(x))

print(type(x).__name__)


"""
<class 'list'>
<class 'list'>
list
"""
