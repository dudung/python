import statistics as s

x = [1, 2, 3, 4, 5, 6, 7]
median = s.median(x)
print(x)
print("median =", median)

print()

y = [1, 1, 3, 3, 4, 8, 10]
median = s.median(y)
print(y)
print("median =", median)

print()

z = [ 1, 2, 3, 3, 80, 100]
median = s.median(z)
print(z)
print("median =", median)


"""
$ python median.py
[1, 2, 3, 4, 5, 6, 7]
median = 4

[1, 1, 3, 3, 4, 8, 10]
median = 3

[1, 2, 3, 3, 80, 100]
median = 3.0
"""
