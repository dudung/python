import sys
sys.path.append("../")

from linked_list_v2.linkedlist_v2 import LinkedList

ll = LinkedList(); print(ll.list())
ll.append(9);      print(ll.list())
ll.insert(0, 7);   print(ll.list())
ll.insert(2, 11);  print(ll.list())
ll.insert(1, 8);   print(ll.list())
ll.insert(3, 10);  print(ll.list())
ll.insert(10, 12); print(ll.list())
ll.insert(0, 6);   print(ll.list())
ll.prepend(5);     print(ll.list())

"""
$ python import_linkedlistv2.py
[]
[9]
[7, 9]
[7, 9, 11]
[7, 8, 9, 11]
[7, 8, 9, 10, 11]
[7, 8, 9, 10, 11, 12]
[6, 7, 8, 9, 10, 11, 12]
[5, 6, 7, 8, 9, 10, 11, 12]
"""
