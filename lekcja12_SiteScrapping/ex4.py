from bs4 import BeautifulSoup
import urllib3
import pandas as pd


url = "https://www.metacritic.com/browse/games/genre/metascore/strategy/all?view=detailed"
http = urllib3.PoolManager()
page = http.request("GET", url)
# wyświetla każdy odczytany bajt
soup = BeautifulSoup(page.data, 'lxml')

score = []
score2 = []
title = []
platform = []
data = []
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

print(df)
