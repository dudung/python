import sys
sys.path.append("../")

from getter_setter.id4d_property_v2 import Id4d

id = Id4d(4)
print(id)

id.value = 91
print(id)

id.value = 632
print(id)

id.value = 4078
print(id)

"""
$ python import_id4d.py
0004
0091
0632
4078
"""
