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

print(ll.head)
print(ll.head.next)
print(ll.head.next.next)
print(ll.head.next.next.next)


"""
$ python append_node.py
nodes=3
value=satu
value=dua
value=tiga
None
"""
