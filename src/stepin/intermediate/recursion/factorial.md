# factorial
$$\tag{1}
n! = n \cdot (n-1) \cdot (n-2) \cdot \ . . . \ \cdot 3 \cdot 2 \cdot 1
$$

$$\tag{2}
n! \equiv f(n) = \left\{
\begin{array}{cc}
1, & n = 0 \newline
n \cdot f(n-1), & n > 0
\end{array}
\right.
$$


```shell
python factorial.py
n       n!
0       1
1       1
2       2
3       6
4       24
5       120
6       720
7       5040
8       40320
9       362880
```


```python
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print("n\tn!")
for n in range(10):
  print(n, factorial(n), sep='\t')

```

