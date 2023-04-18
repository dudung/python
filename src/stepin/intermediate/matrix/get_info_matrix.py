import matrix as mtx

a = [
  [1, 2, 3, 4, 5, 6, 8]
]
print(a)
rnum, cnum = mtx.getinfo(a)
print(rnum, cnum)
print()

b = [
  [1],
  [2],
  [3]
]
print(b)
rnum, cnum = mtx.getinfo(b)
print(rnum, cnum)
print()

c = [
  [1, 0],
  [0, 1]
]
print(c)
rnum, cnum = mtx.getinfo(c)
print(rnum, cnum)


"""
get_info_matrix.py
[[1, 2, 3, 4, 5, 6, 8]]
1 7

[[1], [2], [3]]
3 1

[[1, 0], [0, 1]]
2 2
"""
