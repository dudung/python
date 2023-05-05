# subplots_scatter
```python
import matplotlib.pyplot as plt
import math as m

plt.style.use("_mpl-gallery")

x = [m.cos(m.radians(i*10)) for i in range(37)]
y = [m.sin(2 * m.radians(i*10)) for i in range(37)]

fig, ax = plt. subplots()

ax.scatter(x, y, c='r', s=10)

plt.show()
```


```shell
$ python subplots_scatter.py
```


![](svg/subplots_scatter.svg)
