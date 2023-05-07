# quadratic
$i$ | $x$ | $\Delta x$ | $\Delta^2 x$
:-: | :-: | :-: | :-: |
1 |  3 |    |
2 |  7 |  4 |
3 | 13 |  6 | 2
4 | 21 |  8 | 2
5 | 31 | 10 | 2
6 | 43 | 12 | 2
7 | 57 | 14 | 2

$$\tag{1}
x_{i+1} = x_i + \Delta x_{i+1}
$$

$$\tag{2}
\Delta x_{i+1} = \Delta x_i + \Delta^2 x
$$

$$\tag{3}
x_{i+1} = x_i + \Delta x_i + \Delta^2 x
$$

$$\tag{4}
\begin{array}{rcl}
x_2 & = & x_1 + \Delta x_1 \newline
& = & x_1 + \Delta x_1 + 0 \Delta^2 x
\end{array}
$$

$$\tag{5}
\begin{array}{rcl}
x_3 & = & x_2 + \Delta x_2 \newline
& = & (x_1 + \Delta x_1) + (\Delta x_1 + \Delta^2 x) \newline
& = & x_1 + 2 \Delta x_1 + \Delta^2 x \newline
& = & x_1 + 2 \Delta x_1 + 1 \Delta^2 x
\end{array}
$$

$$\tag{6}
\begin{array}{rcl}
x_4 & = & x_3 + \Delta x_3 \newline
& = & (x_2 + \Delta x_2) + (\Delta x_2 + \Delta^2 x) \newline
& = & x_2 + 2 \Delta x_2 + \Delta^2 x \newline
& = & (x_1 + \Delta x_1) + 2 (\Delta x_1 + \Delta^2 x) + \Delta^2 x \newline
& = & x_1 + 3 \Delta x_1 + 3 \Delta^2 x
\end{array}
$$

$$\tag{7}
\begin{array}{rcl}
x_5 & = & (x_1 + 3 \Delta x_1 + 3 \Delta^2 x) + (\Delta x_3 + \Delta^2 x) \newline
& = & x_1 + 3 \Delta x_1 + \Delta x_3 + 4 \Delta^2 x \newline
& = & x_1 + 3 \Delta x_1 + (\Delta x_2 + \Delta^2 x) + 4 \Delta^2 x \newline
& = & x_1 + 3 \Delta x_1 + \Delta x_2 + 5 \Delta^2 x \newline
& = & x_1 + 3 \Delta x_1 + (\Delta x_1 + \Delta^2 x) + 5 \Delta^2 x \newline
& = & x_1 + 4 \Delta x_1 + 6 \Delta^2 x
\end{array}
$$

$$\tag{8}
\begin{array}{rcl}
x_i & = & x_1 + (i-1) \Delta x_1 + \tfrac12 (i-2)(i-1) \Delta^2 x
\end{array}
$$