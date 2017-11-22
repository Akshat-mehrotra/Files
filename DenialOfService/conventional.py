
import threading
import time
from queue import Queue
import urllib3.request


print_lock = threading.Lock()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def exampleJob(worker):
   # time.sleep(0.05)
    h=urllib3.PoolManager()
    r=h.request('GET','http://www.lviscampuscare.in').read()
   #time.sleep(0.05)
    with print_lock:
        print(threading.current_thread().name,worker)

def threader():
    while True:
        worker = q.get()

        exampleJob(worker)

        q.task_done()

q=Queue()        
for x in range(10010):
    t = threading.Thread(target=threader)

             
    t.daemon = True

             
    t.start()

while True:
    for worker in range(20):
        q.put(worker)


q.join()
