import statistics as s

x = [1, 2, 3, 4, 5, 6, 7]
mean = s.mean(x)
print(x)
print("mean =", mean)

print()

y = [1, 2, 3, 4, 5, 6]
mean = s.mean(y)
print(y)
print("mean =", mean)


"""
$ python mean.py
[1, 2, 3, 4, 5, 6, 7]
mean = 4

[1, 2, 3, 4, 5, 6]
mean = 3.5
"""
