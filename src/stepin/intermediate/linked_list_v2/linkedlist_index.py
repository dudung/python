from linkedlist import LinkedList

ll = LinkedList()
ll.append('A')
ll.append(9)
ll.append('B')
ll.append(True)
ll.append(121)

print(ll.count)
print(ll.list())
print()

print(True, "is at", ll.index(True))
print(121, "is at", ll.index(121))
print('A', "is at", ll.index('A'))
print('B', "is at", ll.index('B'))
print(9, "is at", ll.index(9))

"""
$ python linkedlist_index.py
5
['A', 9, 'B', True, 121]

True is at 3
121 is at 4
A is at 0
B is at 2
9 is at 1
"""
