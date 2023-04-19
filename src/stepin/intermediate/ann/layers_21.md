# layers_21
```mermaid
flowchart LR
  subgraph X<sub>1</sub>
    direction LR
    x11((x<sub>11</sub>))
    x12((x<sub>12</sub>))
  end
  subgraph X<sub>2</sub>
    direction LR
    x21((x<sub>21</sub>))
  end
  x11 --> x21
  x12 --> x21
```

$$
\mathbf{X}_2 = f(\mathbf{W}_{21} \mathbf{X}_1)
$$