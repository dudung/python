from linkedlist import LinkedList

ll = LinkedList()
ll.append(100)
ll.append("Hello")
ll.append(True)
ll.append(98.34E-4)

print(ll.count)
print(ll.list())


"""
$ python linkedlist_append.py
4
[100, 'Hello', True, 0.009834]
"""
