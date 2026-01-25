from threading import Thread,Lock
import time
import sys

lock = Lock()
print = lambda x: sys.stdout.write("%s\n" % x)

def func1():
    print("Thread 1 is aquiring lock")
    with lock:
        print("Thread 1 has aquired the lock")
        time.sleep(3)
    print("Thread 1 has released Lock")

def func2():
    print("Thread 2 is aquiring lock")
    with lock:
        print("Thread 2 has aquired the lock")
        time.sleep(3)
    print("Thread 2 has released Lock")

thread1 = Thread(target=func1)
thread2 = Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()