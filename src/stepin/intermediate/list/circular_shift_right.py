x = [1, 2, 3, 4, 5]
print(x)

y = x.pop()
print(x)
x.insert(0, y)
print(x)


"""
python circular_shift_right.py
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
[5, 1, 2, 3, 4]
"""
