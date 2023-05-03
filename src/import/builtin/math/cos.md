# cos
$$\tag{1}
y = \cos x
$$

$x$ | $y$
:-: | :-:
$0$ | $1$
$\frac16\pi$ | $\frac12\sqrt{3}$
$\frac13\pi$ | $\frac12$
$\frac12\pi$ | $0$


```shell
$ python cos.py
θ(°)    θ(rad)  cos θ
0       0.000π  1.000
30      0.167π  0.866
60      0.333π  0.500
90      0.500π  0.000
120     0.667π  -0.500
150     0.833π  -0.866
180     1.000π  -1.000
210     1.167π  -0.866
240     1.333π  -0.500
270     1.500π  -0.000
300     1.667π  0.500
330     1.833π  0.866
```


```python
import math

angs = [(i / 12) * 2 * math.pi for i in range(12)]

print("θ(°)", "θ(rad)", "cos θ", sep='\t')
for x in angs:
  c1 = f"{(x / math.pi * 180):.0f}"
  c2 = f"{(x / math.pi):.3f}π"
  c3 = f"{math.cos(x):.3f}"
  print(c1, c2, c3, sep='\t')
```
