import actfunc as af
from network import Network
from data import dataset1 as set1

ann = Network("ANN_test_0")

ann.add_input_layer(2)
ann.add_hidden_layer(4, af.sigmoid)
ann.add_hidden_layer(3, af.relu)
ann.add_output_layer(1, af.linear)

ann.add_dataset(set1[1:-14], set="validation")
ann.add_dataset(set1[-14:], set="testing")
ann.add_dataset(set1[0:1], set="training")

print(ann)


"""
$ python net_instantiate.py
ANN_test_0
Layers: [2, 4, 3, 1]
Functions: ['sigmoid', 'relu', 'linear']
Training set: 1
Validation set: 1
Testing set: 14
"""
