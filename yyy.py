import requests
import time
import threading

num = 0

def send():
    global num
    for i in range(10):
        requests.get("http://localhost:8000/look")
        num+=1
        print(num)

count = 100
t = []
start = time.time()
for i in range(count):
    t.append(threading.Thread(target=send))
for i in t:
    i.start()
for i in t:
    i.join()
print(time.time()-start)