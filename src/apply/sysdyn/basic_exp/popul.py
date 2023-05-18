def birth_rate(t2=1, dt=1):
  """
  2 = (1 + b * dt)**(t2/dt)
  2**(dt/t2) = 1 + b * dt
  b * dt = 2**(dt/t2) - 1
  """
  b = (2**(dt/t2) - 1) / dt
  return b

def death_rate(t05=1, dt=1):
  """
  0.5 = (1 - d * dt)**(t05/dt)
  0.5**(dt/t05) = 1 - d * dt
  d * dt = 1 - 0.5**(dt/t05)
  """
  d = (1 - 0.5**(dt/t05)) / dt
  return d
