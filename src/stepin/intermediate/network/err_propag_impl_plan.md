# err_propag_impl_plan
plan for implementation

## architecture
$\color{#00f}\mathbf{I}$<br>$l=1$<br>$m=3$ | $\color{#00f}\mathbf{H}_1$<br>$l = 2$<br>$m=5$ | $\color{#00f}\mathbf{H}_2$<br>$l = 3$<br>$m=4$ | $\color{#00f}\mathbf{H}_3$<br>$l = 4$<br>$m=3$ | $\color{#00f}\mathbf{O}$<br>$l=5$<br>$m=2$
:-: | :-: | :-: | :-:| :-:
&nbsp;  | $x_1^2$ | $x_1^3$ | $x_1^4$ | &nbsp;
$x_2^1$ | $x_2^2$ | $x_2^3$ | &nbsp;  | $x_1^5$
$x_3^1$ | $x_3^2$ | &nbsp;  | $x_2^4$ | &nbsp;
$x_1^1$ | $x_4^2$ | $x_3^3$ | &nbsp;  | $x_2^5$
&nbsp;  | $x_5^2$ | $x_4^3$ | $x_1^4$ | &nbsp;
$\color{#f00}\mathbf{X}_1$ | $\color{#f0f}\mathbf{X}_2$ | $\color{#ff0}\mathbf{X}_3$ | $\color{#0ff}\mathbf{X}_4$ | $\color{#0f0}\mathbf{X}_5$


## feedforward
$$
\begin{array}{rcl}
\color{#f0f}\mathbf{X}_2 & = & f(\mathbf{W}_{21} \color{#f00}\mathbf{X}_1) \newline
\color{#ff0}\mathbf{X}_3 & = & f(\mathbf{W}_{32} \color{#f0f}\mathbf{X}_2) \newline
\color{#0ff}\mathbf{X}_4 & = & f(\mathbf{W}_{43} \color{#ff0}\mathbf{X}_3) \newline
\color{#0f0}\mathbf{X}_5 & = & f(\mathbf{W}_{54} \color{#0ff}\mathbf{X}_4)
\end{array}
$$