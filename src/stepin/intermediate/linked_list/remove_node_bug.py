from node import Node
from linkedlist import LinkedList

ll = LinkedList()

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")

ll.append(n1)
print(ll.graphs())

ll.append(n2)
print(ll.graphs())

ll.append(n3)
print(ll.graphs())

ll.remove(0)
print(ll.graphs())


"""
$ python remove_node_bug.py
A
A --> B
A --> B --> C
A --> B --> C
"""
