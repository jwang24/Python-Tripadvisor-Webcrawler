from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as req

#Sample test
#my_url='https://www.tripadvisor.ca/Hotel_Review-g60763-d2079052-Reviews-YOTEL_New_York-New_York_City_New_York.html'



#This class will grab all the links we want to scrape
class Link_Finder():
    def __init__(self,url):
        page_client = req(url)
        page_html = page_client.read()
        page_client.close()
        page_soup = bs(page_html,"lxml")
        search = page_soup.find('div', id='taplc_location_reviews_list_resp_hr_resp_0')
        self.url = url
        self.links = set()
        self.search = search

    def pagelinks(self):
        for link in self.search.find_all('a',class_='title ',href=True):
            url='https://tripadvisor.ca'+link['href']
            self.links.add(url)
        return self.links






