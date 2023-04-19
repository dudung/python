# layers_2321
```mermaid
flowchart LR
  subgraph X<sub>1</1>
    direction LR
    x11((x<sub>11</sub>))
    x12((x<sub>21</sub>))
  end
  subgraph X<sub>2</sub>
    direction LR
    x21((x<sub>11</sub>))
    x22((x<sub>21</sub>))
    x23((x<sub>31</sub>))
  end
  subgraph X<sub>3</sub>
    direction LR
    x31((x<sub>11</sub>))
    x32((x<sub>21</sub>))
  end
  subgraph X<sub>4</sub>
    direction LR
    x41((x<sub>11</sub>))
  end
  x11 --"w<sub>11</sub>"--> x21
  x12 --"w<sub>12</sub>"--> x21
  x11 --"w<sub>21</sub>"--> x22
  x12 --"w<sub>22</sub>"--> x22
  x11 --"w<sub>31</sub>"--> x23
  x12 --"w<sub>32</sub>"--> x23
  x21 --"w<sub>11</sub>"--> x31
  x22 --"w<sub>12</sub>"--> x31
  x23 --"w<sub>13</sub>"--> x31
  x21 --"w<sub>21</sub>"--> x32
  x22 --"w<sub>22</sub>"--> x32
  x23 --"w<sub>23</sub>"--> x32
  x31 --"w<sub>11</sub>"--> x41
  x32 --"w<sub>12</sub>"--> x41
```

$$\tag{1}
\mathbf{X}^{(3×1)}_2 = f(\mathbf{W}_{21}^{(3×2)} \mathbf{X}_1^{(2×1)})
$$

$$\tag{2}
\mathbf{X}^{(2×1)}_3 = f(\mathbf{W}_{32}^{(2×3)} \mathbf{X}_2^{(3×1)})
$$

$$\tag{3}
\mathbf{X}^{(1×1)}_4 = f(\mathbf{W}_{43}^{(1×2)} \mathbf{X}_3^{(2×1)})
$$

$$\tag{4}
f(z) = \frac{1}{1 + e^{-z}}
$$
