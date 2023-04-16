from linkedlist import LinkedList

ll = LinkedList()
ll.append(True)
ll.append("Hello")
ll.append(98.34E-4)
ll.append(100)

print(ll.count)
print(ll.list())
print()

x = ll.pop()
print(x)
print(ll.count)
print(ll.list())
print()

x = ll.pop()
print(x)
print(ll.count)
print(ll.list())
print()

x = ll.pop()
print(x)
print(ll.count)
print(ll.list())
print()

x = ll.pop()
print(x)
print(ll.count)
print(ll.list())
print()

x = ll.pop()
print(x)
print(ll.count)
print(ll.list())


"""
$ python linkedlist_instance.py
4
[100, 'Hello', True, 0.009834]
"""
