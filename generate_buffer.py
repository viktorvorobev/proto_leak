from random import randint
from foo_pb2 import Foo, Bar

X = Bar.X
Y = Bar.X.Y

foo = Foo()

for i in range(100000):
    bar = Bar()
    for j in range(10):
        x = X()
        for k in range(10):
          x.y.add(value=randint(0, 100))
        bar.x.extend([x])
    foo.bar.extend([bar])

with open("buffer", "wb") as fd:
    fd.write(foo.SerializeToString())
