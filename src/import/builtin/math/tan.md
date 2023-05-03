# tan
$$\tag{1}
y = \tan x
$$

$x$ | $y$
:-: | :-:
$0$ | $0$
$\frac16\pi$ | $\frac13\sqrt{3}$
$\frac13\pi$ | $\sqrt{3}$
$\frac12\pi$ | $\infty, -\infty$


```shell
$ python tan.py
θ(°)    θ(rad)  tan θ
0       0.000π  0.000
30      0.167π  0.577
60      0.333π  1.732
90      0.500π  16331239353195370.000
120     0.667π  -1.732
150     0.833π  -0.577
180     1.000π  -0.000
210     1.167π  0.577
240     1.333π  1.732
270     1.500π  5443746451065123.000
300     1.667π  -1.732
330     1.833π  -0.577
```


```python
import math

angs = [(i / 12) * 2 * math.pi for i in range(12)]

print("θ(°)", "θ(rad)", "tan θ", sep='\t')
for x in angs:
  c1 = f"{(x / math.pi * 180):.0f}"
  c2 = f"{(x / math.pi):.3f}π"
  c3 = f"{math.tan(x):.3f}"
  print(c1, c2, c3, sep='\t')
```
