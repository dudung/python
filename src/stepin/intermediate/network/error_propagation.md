# error_propagation
some equations to perform error propagation


## temporary
From (A4)
$$\tag{B4}
\begin{array}{rcl}
\delta^l_j & = & \displaystyle \frac{\partial C}{\partial z^l_j} \newline
& = & \displaystyle \sum_k \frac{\partial C}{\partial z^{l+1}_k} \ \frac{\partial z^{l+1}_k}{\partial z^l_j} \newline
& = & \displaystyle \sum_k \left( \frac{\partial z^{l+1}_k}{\partial z^l_j} \right) \left( \frac{\partial C}{\partial z^{l+1}_k} \right)  \newline
& = & \displaystyle \sum_k \left[ w_{kj}^{l+1} \ \sigma'(z_j^l) \right] \left( \delta^{l+1}_k \right) \newline
& = & \displaystyle \sum_k w_{kj}^{l+1} \ \sigma'(z_j^l) \ \delta^{l+1}_k
\end{array}
$$



From (A2) and (A3)
$$\tag{B3}
\begin{array}{rcl}
z_j^l & = & \displaystyle b_j^l + \sum_k w_{jk}^l \ \sigma(z_k^{l-1}) \newline
\displaystyle \frac{\partial z_j^l}{\partial z_k^{l-1}} & = & \displaystyle \frac{\partial}{\partial z_k^{l-1}} \left[ b_j^l + \sum_k w_{jk}^l \ \sigma(z_k^{l-1}) \right] \newline
& = & \displaystyle w_{jk}^l \ \frac{\partial}{\partial z_k^{l-1}} \ \sigma(z_k^{l-1}) \newline
& = & w_{jk}^l \ \sigma'(z_k^{l-1}) \newline
\displaystyle \frac{\partial z_j^{l+1}}{\partial z_k^l} & = & w_{jk}^{l+1} \ \sigma'(z_k^l), \ \ \ \ \ \ \ l \rightarrow l + 1\newline
\displaystyle \frac{\partial z_k^{l+1}}{\partial z_j^l} & = & w_{kj}^{l+1} \ \sigma'(z_j^l), \ \ \ \ \ \ \ j \leftrightarrow k
\end{array}
$$


## appendix a
Quadratic cost function of $L$ layers network for a single training example is

$$\tag{A1}\label{A1}
C = \frac12 \sum_j (y_j - a^L_j)^2
$$

with the activation $a_j^L$ of the $j^{\rm th}$ neuron in the $L^{\rm th}$ layer, which is output of the network and $y_j$ is the corresponding desired output of the $j^{\rm th}$ neuron.

An intermediate quantity

$$\tag{A2}
z_j^l = b_j^l + \sum_k w_{jk}^l \ a_k^{l-1}
$$

is the weighted input to the activation function for neuron $j$ in layer $l$, that produces

$$\tag{A3}
a^l_j = \sigma(z_j^l)
$$

where $\sigma$ is activation function.

It can be defined

$$\tag{A4}\label{A4}
\delta^l_j \equiv \frac{\partial C}{\partial z^l_j}
$$

as error of neuron $j$ in layer $l$.

And

$$\tag{A5}
\frac{\partial y}{\partial x} = \frac{\partial y}{\partial u} \ \frac{\partial u}{\partial x}
$$

is known as chain rule.

In the layer $L$ or the output layer

$$\tag{A6}\label{A6}
\delta^L_j \equiv \frac{\partial C}{\partial a^L_j} \sigma'(z^L_j)
$$

can be obtained.


## appendix b
Using equation in Appendix A we can have following derivation

$$\tag{B1}
\begin{array}{rcl}
\delta^l_j & = & \displaystyle \frac{\partial C}{\partial z^l_j} \newline
& = & \displaystyle \frac{\partial C}{\partial a^l_j} \ \frac{\partial a^l_j}{\partial z^l_j} \newline
& = & \displaystyle \frac{\partial C}{\partial a^l_j} \ \frac{\partial \sigma(z^l_j)}{\partial z^l_j} \newline
& = & \displaystyle \frac{\partial C}{\partial a^l_j} \ \sigma'(z^l_j) \newline
\delta^L_j & = & \displaystyle \frac{\partial C}{\partial a^L_j} \ \sigma'(z^L_j)
\end{array}
$$

which gives ($\ref{A6}$) from ($\ref{A4}$).

From ($\ref{A1}$)

$$\tag{B2}
\begin{array}{rcl}
\displaystyle \frac{\partial C}{\partial a^L_j} & = & \displaystyle \frac{\partial }{\partial a^L_j} \left( \frac12 \sum_j (y_j - a^L_j)^2 \right) \newline
& = & \displaystyle \frac12 \cdot 2 \cdot (y_j - a^L_j) \cdot -1 \newline
& = & -(y_j - a^L_j)
\end{array}
$$

can be obtained.
