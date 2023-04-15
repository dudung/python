from node import Node
from linkedlist import LinkedList

ll = LinkedList()

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")

ll.append(n1)
print(ll.graphs())

ll.append(n2)
print(ll.graphs())

ll.append(n3)
print(ll.graphs())

ll.append(n4)
print(ll.graphs())

ll.remove(4)
print(ll.graphs())

ll.remove(2)
print(ll.graphs())

ll.append(n3)
print(ll.graphs())


"""
$ python remove_node.py
A
A --> B
A --> B --> C
A --> B --> C --> D
A --> B --> C --> D
A --> B --> D
A --> B --> D --> C
"""
