from node import Node

n = Node("192.168.20.2")
print(n)

n.data = 1.234E56
print(n)

n.data = False
print(n)

n.data = [-1, "Hello", 'A']
print(n)


"""
$python node_instance.py
192.168.20.2
1.234e+56
False
[-1, 'Hello', 'A']
"""
