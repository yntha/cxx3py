# cxx3py
This tool will convert all structures in a c/c++ header file into python
dataclasses. It will also add a class variable to each dataclass called 'format'
(using a decorator called cxx3py) that can be used as the format string to 
`struct.unpack()` to parse this struct:

From input [test.h](samples/test.h):
```c
typedef struct Il2CppArraySize
{
    Il2CppObject obj;
    Il2CppArrayBounds *bounds;
    il2cpp_array_size_t max_length;
    __attribute__((aligned(8))) void* vector[32];
} Il2CppArraySize;
```
From output [test.py](samples/test.py):
```py
# L1601: struct Il2CppArraySize {...};
@dataclass
@cxx3py("PPPL32P")
class Il2CppArraySize:
  # Il2CppObject obj;
  obj: Il2CppObject # Format: "PP"

  # Il2CppArrayBounds *bounds;
  bounds: int # Format: "P"

  # il2cpp_array_size_t max_length;
  max_length: int # Format: "L"

  # void *[32] vector;
  vector: list # Format: "32P"
```
Note: this is a relatively small script I hacked together. I plan on expanding
this tool even more in the future, but for now it satisfies my needs. I'll
update it here and there as my needs require more. It is a flawed and easy to
break tool, so please don't rely on it heavily.