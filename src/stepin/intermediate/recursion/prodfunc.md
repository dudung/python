# prodfunc
$$\tag{1}
\prod_{i = 0}^n (2i+1) = (2n + 1) \cdot (2(n-1) + 1) \cdot ... \cdot 3 \cdot 1
$$

$$\tag{2}
\prod_{i = 0}^n (2i+1) \equiv f(n) = \left\{
\begin{array}{cc}
1, & n = 0 \newline
(2n+1) \cdot f(n-1), & n > 0
\end{array}
\right.
$$

```shell
$ python prodfunc.py
f(x) = 2x + 1
n       f(x)
0       1
1       3
2       15
3       105
4       945
5       10395
6       135135
7       2027025
8       34459425
9       654729075
```


```python
def f(x):
  return (2*x + 1)

def prodfunc(n, f):
  if n == 0:
    return 1
  else:
    return f(n) * prodfunc(n-1, f)


print("f(x) = 2x + 1")
print("n", "f(x)", sep='\t')
for n in range(10):
  print(n, prodfunc(n, f), sep='\t')
```
