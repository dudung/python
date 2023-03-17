x = [1, "Hello", True, 9.876]
y = [i for i in x]

print(x)
print(y)

x[2] = False
x[0] = -x[0]

print(x)
print(y)


"""
[1, 'Hello', True, 9.876]
[1, 'Hello', True, 9.876]
[-1, 'Hello', False, 9.876]
[1, 'Hello', True, 9.876]
"""
