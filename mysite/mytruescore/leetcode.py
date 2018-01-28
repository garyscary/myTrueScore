from bs4 import BeautifulSoup
import requests
class leetcode:
    def __init__(self,username):
        self.username = username
        self.url = "https://leetcode.com/"+username+'/'
        r = requests.get(self.url).content
        self.soup = BeautifulSoup(r)

    # returns string eg. "10 / 750"
    def solvedQuestions(self):
        return self.soup.select('#base_content > div > div > div.col-sm-5.col-md-4 > div:nth-of-type(3) > ul > li:nth-of-type(1) > span')[0]