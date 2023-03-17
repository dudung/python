x = [1, "Hello", True, 9.876]
y = x

print(x)
print(y)

x[2] = False
x[3] = -x[3]

print(x)
print(y)


"""
[1, 'Hello', True, 9.876]
[1, 'Hello', True, 9.876]
[1, 'Hello', False, -9.876]
[1, 'Hello', False, -9.876]
"""
