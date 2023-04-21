import math

# 01
def binary_step(z):
  if z >= 0:
    return 1
  else
    return 0

# 02
def linear(z, a=1):
  return a * z

# 03
def sigmoid(z):
  return 1 / (1 + math.exp(-z))

# 04
def tanh(z):
  return math.tanh(z)

# 05
def relu(z)
  return max(0, z)

# 06
def leaky_relu(z):
  if x >= 0:
    return x
  else
    return 0.01 * x

# 07
def param_relu(z, a=0.1):
  if x >= 0:
    return x
  else
    return a * x

# 08
def elu(z, a=1):
  if x >= 0:
    return x
  else
    return a * (math.exp(x) - 1)

# 09
def selu(z, a=1, b=1):
  if x >= 0:
    return b * x
  else
    return b * a * (math.exp(x) - 1)

# 10
def gelu(z):
  f1 = z + 0.044715 * (z*z*z)
  f2 = math.tanh(math.sqrt(2/math.pi) * f1)
  f3 = 0.5 * z * (1 + f2)
  return f3

# 11
def swish(z, a=1):
  return x * sigmoid(a*x)

# 12
def softsign(z):
  return z / (1 + abs(z))

# 13
def gaussian(z):
  return math.exp(-0.5 * (z*z))

# 14
def cosine(z):
  return math.cos(z)

# 15
def logit(z):
  return log(z / (1 - z))

# 16
def smoothmax(z):
  return math.log(1 + math.exp(z))

# 17
def modif_relu_cos(z):
  return max(0, z) + math.cos(z)

# 18
def modif_relu_sin(z):
  return max(0, z) + math.sin(z)

# 19
def absoule(z):
  return abs(z)

# 20
def lecun_tanh(z):
  return 1.7159 * math.tanh(2 * z / 3)

# 21
def hard_tanh(z):
  return max(-1, min(1, z))

# 22
def bipolar(z):
  if z < 0:
    return -1
  else
    return 1

# 23
def bipolar_sigmoid(z):
  return (1 - math.exp(-z)) / (1 + math.exp(-z))

# 24
def complementary_log_log(z):
  return 1 - exp(-exp(z))

# 25
def piecewise_linear(z, zmin=0, zmax=1):
  a = 1 / (zmax - zmin)
  b = - a * zmin
  
  if z < zmin:
    return 0
  elif z > 1:
    return 1
  else:
    a * z + b

# 26
def softmax(z):
  sum_exp = sum([math.exp(zi) for zi in z])
  val = [(math.exp(zi)/sum_exp) for zi in z]
  return val
