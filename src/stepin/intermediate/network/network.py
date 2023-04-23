import mtxlib as mtx

class Network:
  def __init__(self, name):
    self.name = name
    self.n = 0
    self.layers = []
    self.functions = []
    self.readonly = False
    self.training = []
    self.validation = []
    self.testing = []
    self.matrices = []
    
  def __str__(self):
    lines = f"{self.name}\n"
    lines += f"Layers: {self.layers}\n"
    funcname = [f.__name__ for f in self.functions]
    lines += f"Functions: {funcname}\n"
    lines +=  f"Training set: {len(self.training)}\n"
    lines +=  f"Validation set: {len(self.validation)}\n"
    lines +=  f"Testing set: {len(self.testing)}"
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
  
  def clear_dataset(self):
    self.training = []
    self.validation = []
    self.testing = []
  
  def add_dataset(self, data, set="testing"):
    if set == "testing":
      self.testing.extend(data)
    elif set == "training":
      self.training.extend(data)
    elif set == "validation":
      self.validation.extend(data)
    else:
      pass
  
  def __create_matrices(self):
    if self.readonly:
      for i in range(len(self.layers)-1):
        rnum = self.layers[i+1]
        cnum = self.layers[i]
        m = mtx.zero(rnum, cnum)
        m = mtx.randomized(m)
        mtx.roundmat(m, 3)
        self.matrices.append(m)
