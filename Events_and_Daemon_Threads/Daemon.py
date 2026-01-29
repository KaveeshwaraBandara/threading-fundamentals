# youtube tutorial followed - https://youtu.be/Kae9aV9DO7k?si=fsB6efkDOoArxGxI

import threading
import time
from pathlib import Path

path = Path(__file__).with_name("text.txt")
text = ""

def readFile():
    global text
    while True:
        try:
            text = path.read_text()
        except FileNotFoundError:
            text = "(text.txt not found yet)"
        time.sleep(0.2) 

def printloop():
    for _ in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
t2.join()  
