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

print(9, "is", ll.find(9))
print(False, "is", ll.find(False))

"""
$ python linkedlist_find.py
5
['A', 9, 'B', True, 121]

9 is 9
False is None
"""
