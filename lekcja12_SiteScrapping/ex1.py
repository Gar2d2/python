from lxml import html
import requests

url = "https://boardgamegeek.com/"
data = requests.get(url)
page = html.fromstring(data.text)

path = '//div[@class = "geekcentral_module leftcol"]//div[@class="media-module__body relative"]//a//@ng-href' 


foundElements = page.xpath(path)
for element in foundElements :
   print(element)
   