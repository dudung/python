from device import Keyboard as kbd
from device import Scanner as scn
from device import Printer as prn


k1 = kbd
print(kbd.name)

k2 = kbd("Wireless Keyboard")
print(kbd.name)

s1 = scn
print(scn)

p1 = prn
print(prn)
