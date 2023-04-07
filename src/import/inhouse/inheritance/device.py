class Computer:
  def __init__(self, name="Computer"):
    self.name = name
    self.type = "bidrectional"
    self.devices = []
  
  def add(self, dev):
    self.devices.append(dev)
    dev.status = "connected"
    dev.host = self.name
  
  def list(self):
    lines = ""
    for i in self.devices:
      lines += "> "
      for attr, value in i.__dict__.items():
        lines += attr + " " + value + ", "
      lines += "\n"
    return lines

class Monitor:
  def __init__(self, name="Monitor"):
    self.name = name
    self.type = "output"
    self.status = "disconnected"
    self.host = "none"


class Keyboard:
  def __init__(self, name="Keyboard"):
    self.name = name
    self.type = "input"
    self.status = "disconnected"
    self.host = "none"


class Mouse:
  def __init__(self, name="Mouse"):
    self.name = name
    self.type = "input"
    self.status = "disconnected"
    self.host = "none"


class Printer:
  def __init__(self, name="Printer"):
    self.name = name
    self.type = "output"
    self.status = "disconnected"
    self.host = "none"


class Scanner:
  def __init__(self, name="Scanner"):
    self.name = name
    self.type = "input"
    self.status = "disconnected"
    self.host = "none"


class Network:
  def __init__(self, name="Network"):
    self.name = name
    self.type = "bidirectional"
    self.status = "disconnected"
    self.host = "none"


class Speaker:
  def __init__(self, name="Speaker"):
    self.name = name
    self.type = "output"
    self.status = "disconnected"
    self.host = "none"


class Microphone:
  def __init__(self, name="Microphone"):
    self.name = name
    self.type = "input"
    self.status = "disconnected"
    self.host = "none"


class Camera:
  def __init__(self, name="Camera"):
    self.name = name
    self.type = "input"
    self.zoom = "digital"
    self.status = "disconnected"
    self.host = "none"


class Digitizer:
  def __init__(self, name="Digitizer"):
    self.name = name
    self.type = "input"
    self.status = "disconnected"
    self.host = "none"


class Storage:
  def __init__(self, name="Storage"):
    self.name = name
    self.type = "bidirectional"
    self.status = "disconnected"
    self.host = "none"


class Microscope(Camera):
  def __init__(self, name="Microscope"):
    Camera.__init__(self, name)
    self.zoom = "optical"
