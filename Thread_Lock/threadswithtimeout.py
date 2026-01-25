from threading import Thread,Lock
import time
import sys

lock = Lock()
print = lambda x: sys.stdout.write("%s\n" % x)

def func1():
    lock.acquire()
    time.sleep(10)
    lock.release()

def func2():
    while True:
        if lock.acquire(timeout=2):
            print("Lock was aquired, do the required task")
            lock.release()
            print("Lock was released")
            break
        else:
            print("Timeout, go do something else useful")
            time.sleep(1)

thread1 = Thread(target=func1)
thread2 = Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()