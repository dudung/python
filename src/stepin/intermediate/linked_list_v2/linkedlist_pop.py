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
$ python linkedlist_pop.py
4
[True, 'Hello', 0.009834, 100]

100
3
[True, 'Hello', 0.009834]

0.009834
2
[True, 'Hello']

Hello
1
[True]

True
0
[]


0
[]
"""
