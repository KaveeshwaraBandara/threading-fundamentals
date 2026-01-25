from filelock import FileLock
from threading import Thread, Lock
import time

file = "example.txt"
lockfile = "example.txt.lock"

lock = FileLock(lockfile)

lock.acquire()
print("Lock aquired")
try:
    with open(file, "a") as f:
        f.write("Add some data")
        time.sleep(5)
finally:
    lock.release()