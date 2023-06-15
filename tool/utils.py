import re
import keyword

from clang.cindex import TypeKind, CursorKind

from models import *

tk2prim = {
  TypeKind.BOOL: '?',
  TypeKind.SCHAR: 'b',
  TypeKind.CHAR_S: 'b',
  TypeKind.UCHAR: 'B',
  TypeKind.CHAR_U: 'B',
  TypeKind.SHORT: 'h',
  TypeKind.USHORT: 'H',
  TypeKind.INT: 'i',
  TypeKind.UINT: 'I',
  TypeKind.LONG: 'l',
  TypeKind.ULONG: 'L',
  TypeKind.LONGLONG: 'q',
  TypeKind.ULONGLONG: 'Q',
  TypeKind.FLOAT: 'f',
  TypeKind.DOUBLE: 'd',
  TypeKind.POINTER: 'P'
}

# https://stackoverflow.com/a/1176023
def camel_to_snake(name):
  name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
  
  return unreserve(name)

def is_reserved(name):
  return (name in __builtins__.__dict__ or keyword.iskeyword(name))

def unreserve(name):
  return ('x_' + name if is_reserved(name) else name)

kind2cxxprim = {
  # byte kinds
  TypeKind.CHAR_U: CxxBytePrimitive,
  TypeKind.CHAR_S: CxxBytePrimitive,
  TypeKind.UCHAR: CxxBytePrimitive,
  TypeKind.SCHAR: CxxBytePrimitive,
  
  # int kinds
  TypeKind.CHAR16: CxxIntPrimitive,
  TypeKind.CHAR32: CxxIntPrimitive,
  TypeKind.USHORT: CxxIntPrimitive,
  TypeKind.UINT: CxxIntPrimitive,
  TypeKind.ULONG: CxxIntPrimitive,
  TypeKind.ULONGLONG: CxxIntPrimitive,
  TypeKind.UINT128: CxxIntPrimitive,
  TypeKind.WCHAR: CxxIntPrimitive,
  TypeKind.SHORT: CxxIntPrimitive,
  TypeKind.INT: CxxIntPrimitive,
  TypeKind.LONG: CxxIntPrimitive,
  TypeKind.LONGLONG: CxxIntPrimitive,
  TypeKind.INT128: CxxIntPrimitive,
  TypeKind.POINTER: CxxIntPrimitive,
  
  # float kinds
  TypeKind.FLOAT: CxxFloatPrimitive,
  TypeKind.DOUBLE: CxxFloatPrimitive,
  TypeKind.LONGDOUBLE: CxxFloatPrimitive,
  TypeKind.FLOAT128: CxxFloatPrimitive
}

kind2cxxarr = {
  # byte kinds
  TypeKind.CHAR_U: CxxByteArray,
  TypeKind.CHAR_S: CxxByteArray,
  TypeKind.UCHAR: CxxByteArray,
  TypeKind.SCHAR: CxxByteArray,
  
  # int kinds
  TypeKind.CHAR16: CxxIntArray,
  TypeKind.CHAR32: CxxIntArray,
  TypeKind.USHORT: CxxIntArray,
  TypeKind.UINT: CxxIntArray,
  TypeKind.ULONG: CxxIntArray,
  TypeKind.ULONGLONG: CxxIntArray,
  TypeKind.UINT128: CxxIntArray,
  TypeKind.WCHAR: CxxIntArray,
  TypeKind.SHORT: CxxIntArray,
  TypeKind.INT: CxxIntArray,
  TypeKind.LONG: CxxIntArray,
  TypeKind.LONGLONG: CxxIntArray,
  TypeKind.INT128: CxxIntArray,
  TypeKind.POINTER: CxxIntArray,
  
  # float kinds
  TypeKind.FLOAT: CxxFloatArray,
  TypeKind.DOUBLE: CxxFloatArray,
  TypeKind.LONGDOUBLE: CxxFloatArray,
  TypeKind.FLOAT128: CxxFloatArray,
  
  # record kinds
  TypeKind.RECORD: CxxRecordArray
}