x = [1, 2, 3, 4, 5]
print(x)

y = x.pop(0)
print(x)
x.append(y)
print(x)


"""
python circular_shift_left.py
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[2, 3, 4, 5, 1]
"""
