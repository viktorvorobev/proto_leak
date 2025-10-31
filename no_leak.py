import os

import psutil

import schema_pb2

process = psutil.Process(os.getpid())


def get_rss_MB():
    return (process.memory_full_info().rss / 1024) / 1024


print("Memory consumed at the beginning", get_rss_MB())


for _ in range(10_000_000):
    obj = schema_pb2.value_test_topic()
    obj.ParseFromString(
        b"\x08\x87\xadK\x11\x00\x00\x00\n.7\xd8A\x1a\x90\x03abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc abc "
    )

print("Memory consumed after parsing", get_rss_MB())


print("Memory consumed after deallocating", get_rss_MB())
