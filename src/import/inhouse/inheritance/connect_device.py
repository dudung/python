from device import Computer as com
from device import Printer as prn
from device import Scanner as scn

p1 = prn("Printer_1")
print(p1.name)
print(p1.status)
print()

m1 = scn("Microscope_1")
print(m1.name)
print(m1.status)
print()

pc1 = com("Komputer_A")
pc1.add(p1)
print(pc1.name)
print()

print(p1.name)
print(p1.status)
print(p1.host)
print()

pc2 = com("Komputer_B")
pc2.add(m1)
print(pc2.name)
print()

print(m1.name)
print(m1.status)
print(m1.host)
print()
