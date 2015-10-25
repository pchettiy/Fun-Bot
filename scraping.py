from bs4 import BeautifulSoup
import requests

class scraper():
    def scrapejoke(self):
                r=requests.get("http://www.rinkworks.com/jokes/random.cgi")
                soup=BeautifulSoup(r.content)
                data=soup.find_all("div",{"class":"content"})
                joke=""
                for item in data:
                    for lines in item.find_all("li"):
                        if lines.parent.name=="ul":
                            joke=joke+lines.text+"\n"
                return joke
    def scrapefact(self):
                r=requests.get("http://facts.randomhistory.com/")
                soup=BeautifulSoup(r.content)
                data=soup.find_all("div",{"class":"home-text"})
                fact=""
                for item in data:
                    fact=fact+item.text
                return fact.lstrip()
