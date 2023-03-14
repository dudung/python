def fare(km, waitingtime = 0):
  basefee = 7000
  kmfee = km * 4000
  waitingfee = waitingtime * 42000
  fees = basefee + kmfee + waitingfee
  return fees

print(fare(2))
print(fare(2, waitingtime=1))
print(fare(2, 1))


"""
15000
57000
57000
"""
