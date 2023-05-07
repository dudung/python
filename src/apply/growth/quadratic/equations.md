# equations
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
x_i = x_1 + (i-1) \Delta x_1 + \tfrac12 (i-1)(i-2) \Delta^2 x
$$

$$\tag{5}
\Delta x \ge 0, \ \ \ \ \Delta^2 x \ge 0
$$

$$\tag{6}
\Delta x_1 = x_2 - x_1
$$

$$\tag{7}
\delta^2 x_i = x_{i+2} - 2x_{i+1} + x_i 
$$

$$\tag{8}
\Delta^2 x = \overline{\delta^2 x} = \frac{1}{n - 2} \sum_{i=1}^{n-2} \delta x_i
$$

## notes
+ Derivation of (4) using (1)-(3) using backward difference.
+ Calculation of (8) using (6)-(7) using forward difference.
+ Should they be consistent only using one type of FD approach?
