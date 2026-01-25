from filelock import FileLock
from threading import Thread, Lock

file = "example.txt"
lockfile = "example.txt.lock"

lock = FileLock(lockfile)

lock.acquire()
print("Lock aquired")
try:
    with open(file, "a") as f:
        f.write("Add some data")
finally:
    lock.release()