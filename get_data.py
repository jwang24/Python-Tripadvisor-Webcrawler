from bs4 import BeautifulSoup
import urllib.request


#This class will extract the reviews from the links we want to scrape.
#This class will collect the title of the review, the review itself and convert the rating given
# from a bubble display to a number in a string value

class Data_Search():

    def __init__(self,link):
        self.link=link

    def get_info(self):
        response = urllib.request.urlopen(self.link)
        soup = BeautifulSoup(response.read(),"lxml")
        score=''

        for items in soup.find_all(class_="ui_column is-10-desktop is-12-tablet is-12-mobile"):
                rating = ''.join(items.find("span").get('class'))
                title = ''.join(items.find("h1", id="HEADING"))
                review = ''.join(items.find("span",class_='fullText'))

                if rating[-2] is '5':
                    score = '5'
                elif rating[-2] is '4':
                    score = '4'
                elif rating[-2] is '3':
                    score = '3'
                elif rating[-2] is '2':
                    score='2'
                elif rating[-2] is '1':
                    score='1'
                else:
                    score=''

        return score,title,review



