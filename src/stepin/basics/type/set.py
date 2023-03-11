print(type({1, 5.93, True, "Hello"}))

x = {1, 5.93, True, "Hello", 1, 3.93, False, "Hi"}
print(type(x))

print(type(x).__name__)


"""
<class 'set'>
<class 'set'>
set
"""
