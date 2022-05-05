import psutil
import os
import datetime
from schema_pb2 import value_test_topic

process = psutil.Process(os.getpid())

def get_rss_MB():
    return (process.memory_full_info().rss / 1024) / 1024

print("Memory consumed at the beginning", get_rss_MB())

lst = []
for _ in range(1000000):
    event_dt = datetime.datetime.utcnow()
    lst.append(value_test_topic(
        myField1=1234567,
        myField2=event_dt.timestamp(),
        myField3="abc " * 100
    ))

print("Memory consumed after parsed", get_rss_MB())

while len(lst):
    lst.pop()

del lst

print("Memory consumed after deallocating", get_rss_MB())
