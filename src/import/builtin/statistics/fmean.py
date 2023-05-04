import statistics as s

x = [1, 2, 3, 4]
fmean = s.fmean(x)
print(x)
print("fmean =", fmean)

print()

y = [1, 2, 3, 4, 5]
fmean = s.fmean(y)
print(y)
print("fmean =", fmean)


"""
$ python fmean.py
[1, 2, 3, 4]
fmean = 2.5

[1, 2, 3, 4, 5]
fmean = 3.0
"""
