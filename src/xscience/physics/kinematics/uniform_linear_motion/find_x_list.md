# find_x_list
$$\tag{4}
x = (x_0 - v_0 \ t_0) + v_0 \ t
$$


```shell
$  ../../../../../scripts/mdpy.sh diff_xv.md
t0 = [0, 1, 2, 3, 4]
v0 = [2, 1, 3, 1, 2]
x0 = [4, 2, 5, 3, 8]
xh = ['x1', 'x2', 'x3', 'x4', 'x5']

t       x1      x2      x3      x4      x5
0       4       1       -1      0       0
1       6       2       2       1       2
2       8       3       5       2       4
3       10      4       8       3       6
4       12      5       11      4       8
5       14      6       14      5       10
6       16      7       17      6       12
7       18      8       20      7       14
8       20      9       23      8       16
9       22      10      26      9       18

```


```python
t0 = [0, 1, 2, 3, 4]
v0 = [2, 1, 3, 1, 2]
x0 = [4, 2, 5, 3, 8]

N = min(len(t0), len(v0), len(x0))

xh = ['x1', 'x2', 'x3', 'x4', 'x5']
print("t0 =", t0)
print("v0 =", v0)
print("x0 =", x0)
print("xs =", xs)
print()

print("t", *xh, sep='\t')
for t in range(10):
  x = []
  for j in range(N): 
    xj = (x0[j] - v0[j] * t0[j]) + v0[j] * t
    x.append(xj)
  
  print(t, end='\t')
  for j in x:
    print(j, end='\t')
  print()
```
