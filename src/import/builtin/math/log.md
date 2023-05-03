# log

$$\tag{1}
y = ^{e}\log x \equiv \ln x
$$


```shell
$ python log.py
x       y=log(x)
1.000   0.0
2.718   1.0
7.389   2.0
20.086  3.0
54.598  4.0
```


```python
import math

e = math.exp(1)
nums = [e**0, e**1, e**2, e**3, e**4]

print("x", "y=log(x)", sep='\t')
for x in nums:
  y = math.log(x)
  print(f"{x:.3f}", y, sep='\t')
```
