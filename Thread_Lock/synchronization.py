# youtube tutorial followed - https://youtu.be/F3-bJlYWeJc?si=f8MTk-Pqlw3rMCX7 

import threading
import time

x = 8192

lock = threading.Lock()

def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # just for tracking whats happening
    print("Reached the maximum!")
    lock.release()

def half():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()

t1 = threading.Thread(target=half)
t2 = threading.Thread(target=double)

t1.start()
t2.start()