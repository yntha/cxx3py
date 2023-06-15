from clang.cindex import TypeKind, CursorKind

import utils
from models import *

class TypeParser:
  def __init__(self, ctype, model):
    self.ctype = ctype
    self.model = model
    
    self.decl = ctype.get_declaration()
    self.unsugared = ctype.get_canonical()
  
  def get_format(self):
    raise NotImplementedError('')
  
  # translate the type into a python model class
  def translate(self):
    raise NotImplementedError('')

class RecordParser(TypeParser):
  def __init__(self, ctype, model):
    super().__init__(ctype, model)
    
    self.members = self._get_members()
  
  def _get_members(self):
    members = []
    
    for member in self.decl.get_children():
      mtype = member.type
      mdecl = mtype.get_declaration()
      
      if mtype.kind == TypeKind.ELABORATED:
        if self.ctype == mdecl.semantic_parent:
          if mdecl.is_anonymous():
            continue
      
      members.append(member)
    
    return members
  
  def translate(self):
    model = self.model()
    
    # translate members
    members = []
    for member in self.members:
      mtype = member.type
      unsugared = mtype.get_canonical()
      ukind = unsugared.kind
      
      if ukind == TypeKind.POINTER:
        if unsugared.spelling.endswith('char *'):
          members.append((member, CxxString))
        
        return members.append((member, CxxPointer))
      
      if ukind == TypeKind.CONSTANTARRAY:
        arr_type = unsugared.get_array_element_type()
        
        return members.append((member, utils.kind2cxxarr[arr_type.kind]))
      
      if mtype.kind == TypeKind.ELABORATED:
        if ukind == TypeKind.ENUM:
          return members.append((member, CxxEnum))
        if ukind == TypeKind.RECORD:
          return members.append((member, CxxRecord))
      
      if ukind in utils.kind2cxxprim:
        return members.append((member, utils.kind2cxxprim[ukind]))
    
    model.members = members
  
  def get_member_format(self, member):
    raise NotImplementedError('')

class StructParser(RecordParser):
  def __init__(self, ctype):
    super().__init__(ctype, CxxStruct)
  
  def get_format(self):
    return ''.join([self.get_member_format(member) for member in self.members])
  
  def get_member_format(self, member):
    pass

class UnionParser(RecordParser):
  def __init__(self, ctype):
    super().__init__(ctype, CxxUnion)
  
  def get_format(self):
    pass
  
  def get_member_format(self):
    pass