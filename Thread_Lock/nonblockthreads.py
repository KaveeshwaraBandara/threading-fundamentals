from threading import Thread, Lock
import time
import sys

lock = Lock()
print = lambda x: sys.stdout.write("%s\n" % x)

def func1():
    lock.acquire()
    print("Lock has been aquired by Thread1")
    time.sleep(5)
    lock.release()

def func2():
    while True:
        if (lock.acquire(blocking=False)):
            print("Lock has been aquired by Thread2")
            time.sleep(3)
            lock.release()
            print("Thread 2 is done with its required task")
            break
        else:
            print("Just do something else...")
            time.sleep(1)


thread1 = Thread(target=func1)
thread2 = Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()