from finder import Finder
import threading
from queue import Queue
import time

start_time = time.time()

search_list = {"test","mert", "mustafa", "ali", "veli","ahmet", "mehmet", "murat",
               "can", "belge", "crawl", "deneme", "versiyon", "sunum", "son"}

search_area = "/"

thread_number = 2

q = Queue()
f = Finder(search_area)

def create_workers():
    for _ in range(thread_number):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        bas_time = time.time()
        key = q.get()
        f.get_search(threading.current_thread().name, key)
        q.task_done()
        print(time.time() - bas_time)

def create_jobs():
    for search_key in search_list:
        q.put(search_key)
    q.join()
    #search()


def search():
    if len(search_list) > 0:
        create_jobs()


create_workers()
create_jobs()

elapsed_time = time.time() - start_time
print(elapsed_time)
