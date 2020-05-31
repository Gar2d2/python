from bs4 import BeautifulSoup
import urllib3
import pandas as pd


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed&page="
strona = ""


score = []
score2 = []
title = []
platform = []
data = []

for x in range(0, 10):
    strona = str(x)
    newurl = url + strona
    http = urllib3.PoolManager()
    page = http.request("GET", newurl)
    soup = BeautifulSoup(page.data, 'lxml')
    sc = soup.find_all('div', {"class": "title_bump"})
    sc = soup.find_all('div', {"class": "metascore_w large game positive"})
    tit = soup.find_all('a', {"class": "title"})
    plat= soup.find_all('div', {"class": "clamp-details"})
    for i in sc:
        score.append(i.string)
    for i in tit:
        title.append(i.find('h3').string)
    for i in plat:
        platform.append(i.find('span', {"class": "data"}).string.strip())
    for i in plat:
        data.append(i.find('span', {"class":''}).string)
    columns = ['platform', 'title', 'score', 'data']
for i in range(len(score)):
    if i%2 == 0:
        score2.append(score[i])

df = pd.DataFrame(columns = columns)
df['title'] = title
df['score'] = score2
df['platform'] = platform
df['data'] = data
df2 = df.loc[df['platform'] == 'PC']
print(df2)
