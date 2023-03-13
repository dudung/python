print(type({"a":1, "b": 2.3, "c": False, "d": "Hai"}))

x = {"a":1, "b": 2.3, "e": {"c": False, "d": "Hai"}}
print(type(x))

print(type(x).__name__)


"""
<class 'dict'>
<class 'dict'>
dict
"""
