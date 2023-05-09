# quadratic
$i$ | $x$ | $\Delta x$ | $\Delta^2 x$ | $\Delta^3 x$
:-: | :-: | :-: | :-: | :-:
0 | 1 | 3 | 8 | 6 |
1 | 4 | 11 | 14 | 6 |
2 | 15 | 25 | 20 | 6 |
3 | 40 | 45 | 26 | 6 |
4 | 85 | 71 | 32 | 6 |
5 | 156 | 103 | 38 | 6 |
6 | 259 | 141 | 44 | 6 |
7 | 400 | 185 | 50 | 6 |
8 | 585 | 235 | 56 |  |
9 | 820 | 291 |  |  |
10 | 1111 |  |  |  |

$$
\begin{array}{rcl}
\Delta^2 x_3 & = & \Delta^2 x_2 + \Delta^3 x \newline
\Delta x_4 & = & \Delta x_3 + \Delta^2 x_3 \newline
x_5 & = & x_4 + \Delta x_4 \newline
& = & \dots
\end{array}
$$

$$
\begin{array}{rcl}
x_2 & = & x_1 + \Delta x_1 \newline
\Delta x_2 & = & \Delta x_1 + \Delta^2 x_1 \newline
x_3 & = & x_2 + \Delta x_2 \newline
x_3 & = & (x_1 + \Delta x_1) + (\Delta x_1 + \Delta^2 x_1) \newline
& = & x_1 + 2 \Delta x_1 + \Delta^2 x_1
\end{array}
$$

$$
\begin{array}{rcl}
\Delta^2 x_2 & = & \Delta^2 x_1 + \Delta^3 x \newline
\Delta x_3 & = & \Delta x_2 + \Delta^2 x_2 \newline
x_4 & = & x_3 + \Delta x_3 \newline
& = & (x_1 + 2 \Delta x_1 + \Delta^2 x_1) \newline
&& + (\Delta x_2 + \Delta^2 x_2) \newline
& = & x_1 + 2 \Delta x_1 + \Delta^2 x_1 \newline
&& + \Delta x_2 + \Delta^2 x_2 \newline
& = & x_1 + 2 \Delta x_1 + \Delta^2 x_1 \newline
&& + (\Delta x_1 + \Delta^2 x_1) + (\Delta^2 x_1 + \Delta^3 x) \newline
& = & x_1 + 3 \Delta x_1 + 3 \Delta^2 x_1 + \Delta x^3
\end{array}
$$

$$\tag{1}
x_{i+1} = x_i + \Delta x_i
$$

$$\tag{2}
\Delta x_{i+1} = \Delta x_i + \Delta^2 x_i
$$

$$\tag{3}
\Delta^2 x_{i+1} = \Delta^2 x_i + \Delta^3 x
$$
