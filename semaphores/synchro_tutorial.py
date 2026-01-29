# youtube tutorial followed - https://youtu.be/F3-bJlYWeJc?si=f8MTk-Pqlw3rMCX7 

import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10)
    print(f"{thread_number} is now releasing!")
    semaphore.release()

for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)