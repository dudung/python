x = {"a": "1", "b": "3", "c": "2", "d": "8" }

print("i in x, i: ", end='')
for i in x:
    print(i, end=" ")
print()

print("i in x, x[i]: ", end='')
for i in x:
    print(x[i], end=" ")
print()

print("i in x.values(), i: ", end='')
for i in x.values():
    print(i, end=" ")
print()

print("i in keys(), i: ", end='')
for i in x.keys():
    print(i, end=" ")
print()

print("i in items(), i: ", end='')
for i in x.items():
    print(i, end=" ")
print()

print("i, j in items(), i j: ")
for i, j in x.items():
    print(i, j)
print()


"""
i in x, i: a b c d
i in x, x[i]: 1 3 2 8
i in x.values(), i: 1 3 2 8
i in keys(), i: a b c d
i in items(), i: ('a', '1') ('b', '3') ('c', '2') ('d', '8')
i, j in items(), i j:
   a 1
   b 3
   c 2
   d 8
"""
