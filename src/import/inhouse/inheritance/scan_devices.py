from device import Computer as com
from device import Monitor as mon
from device import Keyboard as kbd
from device import Mouse as mos
from device import Printer as prn
from device import Scanner as scn
from device import Network as net
from device import Speaker as spk
from device import Microphone as mic
from device import Camera as cam
from device import Digitizer as pen
from device import Storage as hdd
from device import Microscope as sco

pc1 = com("Komputer_1")
pc1.add(mon())
pc1.add(kbd())
pc1.add(mos())
pc1.add(spk())
pc1.add(mic())
pc1.add(net())
pc1.add(pen())
print(pc1.name)
print(pc1.list())

pc2 = com("Komputer_2")
pc2.add(mon())
pc2.add(kbd())
pc2.add(mos())
pc2.add(net())
pc2.add(pen())
pc2.add(hdd())
pc2.add(cam())
pc2.add(sco())
print(pc2.name)
print(pc2.list())
