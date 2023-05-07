# arithmetic
$$\tag{1}
\begin{array}{rcl}
x_{i+1} & = & x_i + \Delta x
\end{array}
$$

$$
\begin{array}{rcl}
x_2 & = & x_1 + \Delta x \newline
& = & x_1 + (2-1) \Delta x
\end{array}
$$

$$
\begin{array}{rcl}
x_3 & = & x_2 + \Delta x \newline
& = & (x_1 + \Delta x) + \Delta x \newline
& = & x_1 + 2 \Delta x \newline
& = & x_1 + (3-1) \Delta x
\end{array}
$$

$$
\begin{array}{rcl}
x_4 & = & x_3 + \Delta x \newline
& = & (x_2 + \Delta x) + \Delta x \newline
& = & x_2 + 2 \Delta x \newline
& = & (x_1 + \Delta x) + 2 \Delta x \newline
& = & x_1 + 3 \Delta x \newline
& = & x_1 + (4-1) \Delta x \newline
\end{array}
$$

$$\tag{2}
\begin{array}{rcl}
x_i & = & x_1 + (i-1) \Delta x
\end{array}
$$

$$\tag{3}
\begin{array}{rcl}
x_j & = & x_i + (j-i) \Delta x \newline
x_j & = & (j - i) \ \Delta x + x_i \newline
x_j & = & \Delta x \ (j - i) + x_i \newline
\end{array}
$$
