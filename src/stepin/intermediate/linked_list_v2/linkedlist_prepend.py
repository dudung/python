from linkedlist import LinkedList

ll = LinkedList()
ll.prepend(100)
ll.prepend("Hello")
ll.prepend(True)
ll.prepend(98.34E-4)

print(ll.count)
print(ll.list())


"""
$ python linkedlist_prepend.py
4
[0.009834, True, 'Hello', 100]
"""
