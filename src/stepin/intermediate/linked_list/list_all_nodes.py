from node import Node
from linkedlist import LinkedList

n1 = Node("satu")
n2 = Node("dua")
n3 = Node("tiga")

ll = LinkedList()
ll.append(n1)
ll.append(n2)
ll.append(n3)
print(ll)
print(ll.graphs())

"""
$ python list_all_nodes.py
nodes=3
satu --> dua --> tiga
"""
