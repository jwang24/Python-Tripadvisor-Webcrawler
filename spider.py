from urllib.request import urlopen
from url_grab import Link_Finder
from general import *
from get_data import *

#This class acts as the base of the program by creating the files in our directory, gathers the links, stores them to the queue
#and continuously updates the files and the queue. The queue is needed for faster processing as accessing the files constantly would
#make the program incredibly inefficient. However, the files are needed in order to save our crawled links whenever we wish to pause the webscraper.

class Spider:

    #Class Variables
    project_name=''
    base_url='https://www.tripadvisor.ca/Hotel_Review-g60763-d2079052-Reviews-YOTEL_New_York-New_York_City_New_York.html'
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()
    links = set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name = project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file=Spider.project_name+'/queue.txt'
        Spider.crawled_file=Spider.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    @staticmethod
    def boot():
        create_folder(Spider.project_name)
        create_files(Spider.project_name,Spider.base_url)
        Spider.queue = file_set(Spider.queue_file)
        Spider.crawled=file_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(self,thread_name,page_url):
        if page_url not in Spider.crawled:
            print(thread_name+'now crawling '+page_url)
            print('Queue '+str(len(Spider.queue))+'| Crawled '+str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links())
            data = get_info(page_url)
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
        return data

    @staticmethod
    def gather_links():
        for i in range(0, 51, 5):
            my_url = 'https://www.tripadvisor.ca/Hotel_Review-g60763-d2079052-Reviews-or' + str(
                i) + '-YOTEL_New_York-New_York_City_New_York.html'
            test = Link_Finder(my_url)
            create = test.pagelinks()
            for value in create:
                Spider.links.add(value)
        value2= ' '.join(Spider.links)
        return value2

    @staticmethod
    def add_links_to_queue(link):
        for url in link:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if url in Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_file(Spider.queue,Spider.queue_file)
        set_file(Spider.crawled,Spider.crawled_file)






