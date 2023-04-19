# layers_21
```mermaid
flowchart LR
  subgraph X
    direction LR
    x1((x<sub>1</sub>))
    x2((x<sub>2</sub>))
  end
  subgraph Y
    direction LR
    y1((y<sub>1</sub>))
  end
  x1 --"w<sub>11</sub>"--> y1
  x2 --"w<sub>12</sub>"--> y1
```

$$\tag{1}
\mathbf{Y}_{(1×1)} = f(\mathbf{W}_{(1×2)} \mathbf{X}_{(2×1)})
$$

$$\tag{2}
\left[
\begin{array}{c}
y_1
\end{array}
\right] = \left[
\begin{array}{cc}
w_{11} & w_{12}
\end{array}
\right] \left[
\begin{array}{c}
x_1 \newline
x_2
\end{array}
\right]
$$

$$\tag{3}
f(z) = \frac{1}{1 + e^{-z}}
$$
