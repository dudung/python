# equations
$$\tag{A1}
x_{i+1} = x_i + \Delta x_1 + (i - 1) \Delta x'   
$$

(?) $\Delta x_1$ --> $\Delta x_n$

$$\tag{A2}
x_i = x_1 + (i - 1) \Delta x_1 + \tfrac12 i (i - 2) \Delta x' 
$$

(?) $\tfrac12 i (i - 2)$ --> $\tfrac12 (i - 1) (i - 2)$

$$\tag{B1}
x'_{i+1} = x'_i + \Delta x', \ \ \ \ i = 1, \ 2, \ 3, \ \dots, \ n-1
$$

$$\tag{B2}
x'_i = x'_1 + (i - 1)\Delta x', \ \ \ \ i = 1, \ 2, \ 3, \ \dots, \ n-1
$$

$$\tag{B3}
\Delta x' \ge 0
$$

$$\tag{B4}
\delta x'_i = x'_{i+1} - x'_i
$$

$$\tag{B5}
\Delta x' = \overline{\delta x'} = \frac{1}{n - 2} \sum_{i=1}^{n-2} \delta x'_i
$$

$$\tag{C1}
x_{i+1} = x_i + \Delta x, \ \ \ \ i = 1, \ 2, \ 3, \ \dots, \ n
$$

$$\tag{C2}
x_i = x_1 + (i - 1)\Delta x, \ \ \ \ i = 1, \ 2, \ 3, \ \dots, \ n
$$

$$\tag{C3}
\Delta x \ge 0
$$

$$\tag{C4}
\delta x_i = x_{i+1} - x_i
$$

$$\tag{C5}
\Delta x = \overline{\delta x} = \frac{1}{n - 1} \sum_{i=1}^{n-1} \delta x_i
$$
