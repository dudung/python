# sumfunc
$$\tag{1}
\sum_{i = 0}^n i^2 = n^2 + (n-1)^2 + \dots + 2^2 + 1^2 + 0^2
$$

$$\tag{2}
\sum_{i = 0}^n i^2 \equiv f(n) = \left\{
\begin{array}{cc}
0, & n = 0 \newline
n^2 + f(n-1), & n > 0
\end{array}
\right.
$$


```shell
$ python sumfunc.py
f(x) = x^2
n       sumfunc(n,f)
0       0
1       1
2       5
3       14
4       30
5       55
6       91
7       140
8       204
9       285
```


```python
def f(x):
  return x**2

def sumfunc(n, f):
  if n == 0:
    return 0
  else:
    return f(n) + sumfunc(n-1, f)

print("f(x) = x^2")
print("n\tsumfunc(n,f)")
for n in range(10):
  print(n, sumfunc(n, f), sep='\t')
```
