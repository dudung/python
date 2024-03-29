# sin
$$\tag{1}
y = \sin x
$$

$x$ | $y$
:-: | :-:
$0$ | $0$
$\frac16\pi$ | $\frac12$
$\frac13\pi$ | $\frac12\sqrt{3}$
$\frac12\pi$ | $1$


```shell
$ python sin.py
θ(°)    θ(rad)  sin θ
0       0.000π  0.000
30      0.167π  0.500
60      0.333π  0.866
90      0.500π  1.000
120     0.667π  0.866
150     0.833π  0.500
180     1.000π  0.000
210     1.167π  -0.500
240     1.333π  -0.866
270     1.500π  -1.000
300     1.667π  -0.866
330     1.833π  -0.500
```


```python
import math

angs = [(i / 12) * 2 * math.pi for i in range(12)]

print("θ(°)", "θ(rad)", "sin θ", sep='\t')
for x in angs:
  c1 = f"{(x / math.pi * 180):.0f}"
  c2 = f"{(x / math.pi):.3f}π"
  c3 = f"{math.sin(x):.3f}"
  print(c1, c2, c3, sep='\t')
```
