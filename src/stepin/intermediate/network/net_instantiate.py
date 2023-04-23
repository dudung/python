from network import Network

ann = Network()
ann.add_input_layer(2)
ann.add_hidden_layer(4, sigmoid)
ann.add_hidden_layer(3, relu)
ann.add_output_layer(1, linear)
print(ann)
