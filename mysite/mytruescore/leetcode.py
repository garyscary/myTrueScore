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
        return self.tree.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[1]/span/text()')
    def acceptedSubmissions(self):
        return self.tree.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[2]/span/text()')
    def acceptanceRate(self):
        return self.tree.xpath('//*[@id="base_content"]/div/div/div[1]/div[3]/ul/li[3]/span/text()')