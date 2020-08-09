import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup=BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hn):
    return sorted(hn,key= lambda k:k['vote'], reverse=True)

def create_custom_hn(links,subtext):
    hn=[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points>99:
                hn.append({'title':title,'link':href,'vote':points})
    return sort_stories_by_votes(hn)

print(create_custom_hn(links,subtext))