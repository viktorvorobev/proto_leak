import psutil
import os
from foo_pb2 import Foo

process = psutil.Process(os.getpid())

def get_vms_MB():
    return (process.memory_full_info().vms / 1024) / 1024

print("Memory consumed at the beginning", get_vms_MB())

with open("buffer", "rb") as fd:
    foo = Foo()
    foo.ParseFromString(fd.read())

print("Memory consumed after parsed", get_vms_MB())

del(foo)
print("Memory consumed after deallocating", get_vms_MB())


with open("buffer", "rb") as fd:
    foo = Foo()
    foo.ParseFromString(fd.read())

print("Memory consumed after parsed", get_vms_MB())

for bar in foo.bar:
    for x in bar.x:
        pass

print("Memory consumed after iterating", get_vms_MB())

del(foo)

print("Memory consumed after deallocating", get_vms_MB())
