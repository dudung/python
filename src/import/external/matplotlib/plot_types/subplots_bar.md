# subplots_bar
```python
import matplotlib.pyplot as plt
import random as r

plt.style.use("_mpl-gallery")

x = [i for i in range(10)]
y = [r.randint(10, 20) for i in x]

fig, ax = plt. subplots()

ax.bar(x, y, width=1, edgecolor="white")

plt.show()
```


```shell
$ python subplots_bar.py
```


![](svg/subplots_bar.svg)
