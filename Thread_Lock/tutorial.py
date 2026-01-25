from threading import Thread, Lock
import time
import sys

lock = Lock()
print = lambda x: sys.stdout.write("%s\n" % x)

def func1():
    print("Thread 1 is acquiring the lock")
    lock.acquire(timeout=10)
    print("Thread 1 acquired the lock")
    time.sleep(2)  # SOME HEAVY OPERATION IS HAPPENING TO SHARED RESOURCES
    lock.release()
    print("Thread 1 has released the lock")

def func2():
    print("Thread 2 is acquiring the lock")
    lock.acquire()
    print("Thread 2 acquired the lock")
    time.sleep(2)  # SOME HEAVY OPERATION IS HAPPENING TO SHARED RESOURCES
    lock.release()
    print("Thread 2 has released the lock")

thread1 = Thread(target=func1)
thread2 = Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
