import urllib.request
import codecs
import json
from bs4 import BeautifulSoup
import requests

def uva(username):
    # get the number of solved problems
    reader = codecs.getreader("utf-8")
    uid = str(reader(urllib.request.urlopen("https://uhunt.onlinejudge.org/api/uname2uid/"+username)).read())
    submissions = urllib.request.urlopen("https://uhunt.onlinejudge.org/api/subs-user/"+uid)
    obj = json.load(reader(submissions))
    totalsolved = 0
    solvedSet = set()
    for i in obj['subs']:
        if i[2] == 90 and i[0] not in solvedSet:
            solvedSet.add(i[0])
    return len(solvedSet)

def firecode(userid):
    url = "https://www.firecode.io/pages/profile/"
    content = requests.get(url+userid).content
    soup = BeautifulSoup(content, "lxml")
    table = soup.find("table", {"id": "problem-history"}).tbody
    solvedSet = set()
    for tr in table.find_all("tr"):
        problem = ""
        solved = False
        a = tr.find_all('td')[1].find_all('a')
        for i in a:
            problem = i.text.strip()
        b = tr.find_all('td')[2].find_all("img")
        if not b:
            solved = True
        if solved:
            solvedSet.add(problem) 
    return len(solvedSet)
    
class leetcode:
    def __init__(self,username):
        self.username = username
        self.url = "https://leetcode.com/"+username+'/'
        r = requests.get(self.url).content
        self.soup = BeautifulSoup(r)

    # returns string eg. "10 / 750"
    def solvedQuestions(self):
        return self.soup.select('#base_content > div > div > div.col-sm-5.col-md-4 > div:nth-of-type(3) > ul > li:nth-of-type(1) > span')[0]
