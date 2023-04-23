import actfunc as af
from network import Network
from data import dataset1 as set1

ann = Network("ANN_test_1")

ann.add_input_layer(2)
ann.add_hidden_layer(3, af.sigmoid)
ann.add_hidden_layer(4, af.relu)
ann.add_hidden_layer(3, af.sigmoid)
ann.add_output_layer(1, af.linear)

ann.add_dataset(set1[1:-14], set="validation")
ann.add_dataset(set1[-14:], set="testing")
ann.add_dataset(set1[0:1], set="training")

print(ann)

print()
print("Matrices and functions:")
ann.create_matrices()
k = 0
for i in ann.matrices:
  for j in i:
    print(j)
  print(ann.functions[k].__name__)
  k += 1


"""
$ python net_matrix.py
ANN_test_1
Layers: [2, 3, 4, 3, 1]
Functions: ['sigmoid', 'relu', 'sigmoid', 'linear']
Training set: 1
Validation set: 1
Testing set: 14

Matrices and functions:
[0.867, 0.587]
[0.648, -0.225]
[-0.711, -0.087]
sigmoid
[0.613, 0.563, -0.12]
[0.313, 0.269, -0.162]
[0.774, 0.979, -0.995]
[-0.149, 0.432, -0.749]
relu
[-0.25, 0.456, -0.148, 0.303]
[-0.058, -0.869, -0.544, -0.054]
[0.518, 0.602, 0.376, -0.031]
sigmoid
[0.369, 0.639, 0.395]
linear
"""
