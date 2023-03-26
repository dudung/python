<pre><code>```mermaid
  flowchart TB
```</code></pre>

```mermaid
  flowchart TB
    B --> I --> P1 --> P2 --> o1a
    o1b --> o2 --> P3 --> O --> C1 --"N"--> P4 --> C2
    C2 --"Y"--> P5 --> o2
    C1 --"Y"--> o3a
    C2 --"N"--> o3a
    o3b --> E
    B(("Begin"))
    I[/"f(x), xbeg,<br> xend, dx"/]
    P1["x = xbeg"]
    P2["yold = f(xbeg)"]
    P3["y = f(x)"]
    O[/"Print x, y"/]
    E(("End"))
    C1{"yold &middot; y < 0 ?"}
    C2{"x &le; xend ?"}
    P4["yold = y"]
    P5["x = x + dx"]
    o1a(("1")); o1b(("1"));
    o2((" "))
    o3a(("2")); o3b(("3"));
```


```python
def f(x):
  y = (x - 2.3)
  return y

xbeg = 0
xend = 10
dx = 0.5

yold = f(xbeg)
x = xbeg
print("x    y")
while x <= xend:
  y = f(x)
  
  xs = f'{x:.1f}'
  ys = f'{y:+.1f}'
  print(xs, ys)
  
  if y * yold < 0:
    break
  
  yold = y
  
  x += dx
```

```shell
$ python while.py
x    y
0.0 -2.3
0.5 -1.8
1.0 -1.3
1.5 -0.8
2.0 -0.3
2.5 +0.2
```
