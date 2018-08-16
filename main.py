import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

#This is the main part of the program that creates multithreading functionality. Multithreading allows the webscraper to run
#quicker and more efficiently.

PROJECT_NAME='tripadvisor'
HOMEPAGE= 'https://www.tripadvisor.ca/Hotel_Review-g60763-d2079052-Reviews-YOTEL_New_York-New_York_City_New_York.html'
DOMAIN_NAME = get_domain(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME+'/queue.txt'
CRAWLED_FILE = PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# Worker threads (daemon: will end when main thread ends)
def workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=to_do)
        t.daemon = True
        t.start()


# This will run the next task in the queue
def to_do():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# New jobs
def jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# This will crawl items in the queue if they exist
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        jobs()


workers()
crawl()
