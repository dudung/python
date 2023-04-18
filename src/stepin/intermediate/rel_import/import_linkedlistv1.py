import random

import sys
sys.path.append("../")

from linked_list.node import Node
from linked_list.linkedlist import LinkedList

ll = LinkedList()

N = 10
for i in range(N):
  num1 = random.randint(10, 99)
  num2 = random.randint(10, 99)
  n = Node([num1, num2])
  ll.append(n)

print(ll)
print(ll.graphs())


"""
$ python import_linkedlistv1.py
nodes=10
[20, 98] --> [28, 17] --> [82, 66] --> [66, 55] --> [23, 65] --> [75, 81] --> [57, 95] --> [74, 12] --> [53, 81] --> [19, 32]
"""
