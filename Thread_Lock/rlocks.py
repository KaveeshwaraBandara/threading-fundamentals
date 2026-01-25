from threading import Thread, Lock, RLock
import time
import sys

lock = RLock()
print = lambda x: sys.stdout.write("%s\n" % x)

def task2():
    print("Task 2 attempting to aquire the lock")
    lock.acquire()
    print("Task 2 has aquired the lock")
    time.sleep(2)
    lock.release()
    print("Task 2 has released the lock")

def task1():
    print("Task 1 attempting to aquire the lock")
    lock.acquire()
    print("Task 1 has aquired the lock")
    task2()
    lock.release()
    print("Task 1 has released the lock")

def task3():
    print("Task 3 attempting to aquire the lock")
    lock.acquire()
    print("Task 3 has aquired the lock")
    time.sleep(2)
    lock.release()
    print("Task 3 has released the lock")

thread1 = Thread(target=task1)
thread2 = Thread(target=task3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
