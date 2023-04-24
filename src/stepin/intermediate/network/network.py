import mtxlib as mtx
import copy

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
    self.X = None
    self.Y = None
    self.Z = None
  
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
  
  def _create_matrices(self):
    if self.readonly:
      for i in range(len(self.layers)-1):
        rnum = self.layers[i+1]
        cnum = self.layers[i]
        m = mtx.zero(rnum, cnum)
        m = mtx.randomized(m)
        mtx.roundmat(m, 3)
        self.matrices.append(m)
  
  def _prepare_data(self):
    if self.readonly:
      nx = self.layers[0]
      
      x = []
      for i in range(nx):
        x.append([mtx.columnof(i, self.testing)])
      X = mtx.stackrows2(x)
      
      z = mtx.columnof(nx, self.testing)
      Z = [z]
      
      self.X = X
      self.Z = Z
  
  def _feedforward(self):
    if self.readonly:
      X = copy.deepcopy(self.X)
      
      nm = len(self.matrices)
      for i in range(nm):
        W = self.matrices[i]
        f = self.functions[i]
        Y = mtx.map(mtx.mul(W, X), f)
        X = copy.deepcopy(Y)
      
      self.Y = Y
