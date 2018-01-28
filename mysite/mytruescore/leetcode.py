from lxml import html
import requests

class leetcode:
    def __init__(self,username):
        self.username = username
        self.page = requests.get("https://leetcode.com/"+username+'/')
        self.tree = html.fromstring(self.page.content)
    def finishedContests(self):
        return self.tree.xpath('//*[@id="base_content"]/div/div/div[1]/div[2]/ul/li/span/text()')
    def solvedQuestions(self):
        return 
    def acceptedSubmissions(self):
        return
    def acceptanceRate(self):
        return
    def submissionsLastYear(self):
        return
    def recentSubmissions(self):
        # array of problems
        return
    def languages(self):
        return