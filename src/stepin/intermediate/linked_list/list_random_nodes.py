import random
from node import Node
from linkedlist import LinkedList

ll = LinkedList()

N = 20
for i in range(N):
  num = random.randint(10, 99)
  n = Node(num)
  ll.append(n)

print(ll)
print(ll.graphs())


"""
$ python list_random_nodes.py
nodes=20
57 --> 69 --> 81 --> 80 --> 66 --> 33 --> 61 --> 13 --> 23 --> 80 --> 83 --> 87 --> 90 --> 31 --> 78 --> 11 --> 72 --> 42 --> 72 --> 69
"""
