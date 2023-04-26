# err_propag_impl_plan
plan for implementation

## architecture
$\mathbf{I}$<br>$l=1$<br>$m=3$ | $\mathbf{H}_1$<br>$l = 2$<br>$m=5$ | $\mathbf{H}_2$<br>$l = 3$<br>$m=4$ | $\mathbf{H}_3$<br>$l = 4$<br>$m=3$ | $\mathbf{O}$<br>$l=5$<br>$m=2$
:-: | :-: | :-: | :-:| :-:
&nbsp;  | $x_1^2$ | $x_1^3$ | $x_1^4$ | &nbsp;
$x_2^1$ | $x_2^2$ | $x_2^3$ | &nbsp;  | $x_1^5$
$x_3^1$ | $x_3^2$ | &nbsp;  | $x_2^4$ | &nbsp;
$x_1^1$ | $x_4^2$ | $x_3^3$ | &nbsp;  | $x_2^5$
&nbsp;  | $x_5^2$ | $x_4^3$ | $x_1^4$ | &nbsp;
$\color{#f00}\mathbf{X}_1$ | $\color{#f0f}\mathbf{X}_2$ | $\color{#ff0}\mathbf{X}_3$ | $\color{#0ff}\mathbf{X}_4$ | $\color{#0f0}\mathbf{X}_5$


## backpropagation

$$
\begin{array}{rcl}
\mathbf{D}_5^x & = & ({\color{#0f0}\mathbf{X}_5^x} - \mathbf{Y}) \odot f'(\mathbf{W}_{54} \color{#0ff}\mathbf{X}_4^x) \newline
\mathbf{D}_4^x & = & (\mathbf{W}_{54}^T \mathbf{D}_5^x) \odot f'(\mathbf{W}_{43} \color{#ff0}\mathbf{X}_3^x) \newline
\mathbf{D}_3^x & = & (\mathbf{W}_{43}^T \mathbf{D}_4^x) \odot f'(\mathbf{W}_{32} \color{#f0f}\mathbf{X}_2^x) \newline
\mathbf{D}_2^x & = & (\mathbf{W}_{32}^T \mathbf{D}_3^x) \odot f'(\mathbf{W}_{21} \color{#f00}\mathbf{X}_1^x) \newline
\mathbf{W}_{ab} & = & \displaystyle \mathbf{W}_{ab} - \frac{\eta}{m} \sum_{x=1}^m \mathbf{D}_a^x (\mathbf{W}_{ab} \mathbf{X}_b^x)^T
\end{array}
$$


## feedforward
$$
\begin{array}{rcl}
\mathbf{Y}^x & = & \mathbf{Y}^x({\color{#00f}\mathbf{X}^x}) \newline
{\color{#00f}\mathbf{X}} & \rightarrow & {\color{#f00}\mathbf{X}_1^x} \newline
\color{#f0f}\mathbf{X}_2^x & = & f(\mathbf{W}_{21} \color{#f00}\mathbf{X}_1^x) \newline
\color{#ff0}\mathbf{X}_3^x & = & f(\mathbf{W}_{32} \color{#f0f}\mathbf{X}_2^x) \newline
\color{#0ff}\mathbf{X}_4^x & = & f(\mathbf{W}_{43} \color{#ff0}\mathbf{X}_3^x) \newline
\color{#0f0}\mathbf{X}_5^x & = & f(\mathbf{W}_{54} \color{#0ff}\mathbf{X}_4^x) \newline
\color{#f88}\mathbf{C}^x & = & \displaystyle \frac12 \lvert \mathbf{Y}^x - \color{#0f0}\mathbf{X}_5^x \rvert^2
\end{array}
$$