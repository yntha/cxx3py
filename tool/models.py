class CxxType:
  pass

class CxxEnum(CxxType):
  pass

class CxxRecord(CxxType):
  def __init__(self):
    self.members = None

class CxxStruct(CxxRecord):
  pass

class CxxUnion(CxxRecord):
  pass

class CxxPointer(CxxType):
  def __init__(self):
    self.address = None
    self.value = None

class CxxArray(CxxType):
  def __init__(self):
    self.items = None
    self.size = None

class CxxPrimitive(CxxType):
  def __init__(self):
    self.pytype = None

class CxxBytePrimitive(CxxPrimitive):
  pass

class CxxIntPrimitive(CxxPrimitive):
  pass

class CxxFloatPrimitive(CxxPrimitive):
  pass

class CxxByteArray(CxxArray):
  pass

class CxxIntArray(CxxArray):
  pass

class CxxFloatArray(CxxArray):
  pass

class CxxRecordArray(CxxArray):
  pass