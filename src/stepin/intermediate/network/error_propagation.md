# error_propagation
Quadratic cost function of $L$ layers network for a single training example is

$$\tag{1}
C = \frac12 \sum_j (y_j - a^L_j)^2
$$

with the activation $a_j^L$ of the $j^{\rm th}$ neuron in the $L^{\rm th}$ layer, which is output of the network and $y_j$ is the corresponding desired output of the $j^{\rm th}$ neuron.

An intermediate quantity

$$\tag{2}
z_j^l = b_j^l + \sum_k w_{jk}^l \ a_k^{l-1}
$$

is the weighted input to the activation function for neuron $j$ in layer $l$.

It can be defined

$$\tag{3}
\delta^l_j \equiv \frac{\partial C}{\partial z^l_j}
$$

as error of neuron $j$ in layer $l$.

And

$$\tag{4}
\frac{\partial y}{\partial x} = \frac{\partial y}{\partial u} \ \frac{\partial u}{\partial x}
$$

is known as chain rule.


## output layer
In the layer $L$ or the output layer

$$\tag{5}
\delta^L_j \equiv \frac{\partial C}{\partial a^L_j} \sigma'(z^L_j)
$$

can be obtained.
