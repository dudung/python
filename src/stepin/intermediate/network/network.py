class Network:
  def __init__(self):
    self.n = 0
    self.layers = []
    self.functions = []
    self.readonly = False
    
  def __str__(self):
    lines = f"Layers: {self.layers}\n"
    lines += f"Functions: {self.functions}"
    return lines
  
  def add_input_layer(self, num_neurons):
    if self.n == 0 and not self.readonly:
      self.layers.append(num_neurons)
      self.n += 1
  
  def add_hidden_layer(self, num_neurons, act_func):
    if self.n > 0 and not self.readonly:
      self.layers.append(num_neurons)
      self.functions.append(act_func)
      self.n += 1
  
  def add_output_layer(self, num_neurons, act_func):
    if self.n > 0 and not self.readonly:
      self.layers.append(num_neurons)
      self.functions.append(act_func)
      self.n += 1
      self.readonly = True
