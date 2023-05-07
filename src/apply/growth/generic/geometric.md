# geometric
$i$ | $x$ | $x_{i+1}/x_i$
:-: | :-: | :-:
1 |   3 | 2
2 |   6 | 2
3 |  12 | 2
4 |  24 | 2
5 |  48 | 2
6 |  96 | 2
7 | 192 | 2
8 | 384 |

$$\tag{1}
\begin{array}{rcl}
x_{i+1} & = & c \cdot x_i
\end{array}
$$

$$\tag{2}
\begin{array}{rcl}
x_2 & = & c \cdot x_1
\end{array}
$$

$$\tag{3}
\begin{array}{rcl}
x_3 & = & c \cdot x_2 \newline
& = & c \cdot(c \cdot x_1) \newline
& = & c^2 \cdot x_1
\end{array}
$$

$$\tag{4}
\begin{array}{rcl}
x_4 & = & c \cdot x_3 \newline
& = & c \cdot(c \cdot x_2) \newline
& = & c^2 \cdot x_2 \newline
& = & c^2 \cdot (c \cdot x_1) \newline
& = & c^3 \cdot x_1
\end{array}
$$

$$\tag{5}
\begin{array}{rcl}
x_i & = c^{i-1} \cdot x_1
\end{array}
$$

$$\tag{6}
\begin{array}{rcl}
x_i & = c^{i-j} \cdot x_j
\end{array}
$$
