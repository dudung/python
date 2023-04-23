import actfunc as af
from network import Network
from data import dataset1 as set1

ann = Network("ANN_test_2")

ann.add_input_layer(2)
ann.add_hidden_layer(3, af.sigmoid)
ann.add_hidden_layer(4, af.relu)
ann.add_hidden_layer(3, af.sigmoid)
ann.add_hidden_layer(2, af.relu)
ann.add_output_layer(1, af.linear)

ann.add_dataset(set1[1:-14], set="validation")
ann.add_dataset(set1[-2:], set="testing")
ann.add_dataset(set1[0:1], set="training")

ann._create_matrices()
ann._prepare_data()
print("X (input) =", ann.X)
print("Y (calc) =", ann.Y)
print("Z (data) =", ann.Z)


"""
$ python net_data.py
X (input) = [[2, 3], [0, 0]]
Y (calc) = None
Z (data) = [[2], [2]]
"""
