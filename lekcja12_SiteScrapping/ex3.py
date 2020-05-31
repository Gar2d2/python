from lxml import html
import requests
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt


url = "https://boardgamegeek.com/browse/boardgame"
data = requests.get(url)

page = html.fromstring(data.text)
# tabela z grami wszechczasów (tylko pierwsza strona !), pobrana za pomocą XPath
xpath = '//*[@id="collection"]//*[@class="table-responsive"]'
# można pobierać elementy dokumentu również poprzez funkcje pakietu lxml po id lub klasie
table_div = page.get_element_by_id('collection')

# w dowolnym momencie na elemencie ponownie możemy pobrać elementy przez XPath, najważniejsza jest wiedza o drzewie DOM dokumentu w celu określenia odpowiedniej ścieżki względnej lub bezwzględnej 
# należy pamiętać (lub sprawdzić) to, że zostanie zwrócona lista odnalezionych elementów dokumentu, stąd index [0] aby zwrócić bezpośrednio ten element a nie całą listę
table = table_div.xpath('./*[@class="table-responsive"]/table')[0]


# wyświetlamy wszystkie nagłówki tabeli (po przeanalizowaniu dokumentu okazało się, że nie użyto znacznika <thead> do oddzielenia nagłówka tabeli, szukamy więc tylko znaczników <th>)
labels = [label.strip() for label in table.xpath('.//th/text()')]


# kolejna informacja jest taka, że większość (ale nie wszystkie) nagłówków jest w formie łącza (znacznik <a>), trzeba więc wyłuskać z niego tekst
headers = [label for label in table.xpath('.//th')]
xdata = [label for label in table.xpath('//tr//td')]
labels = []
xdataa = []
for header in headers:
    anchor = header.xpath('./a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        labels.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        labels.append(header.text.strip())
for header in xdata:
    anchor = header.xpath('.//a/text()')
    if len(anchor) > 0:
        # znowu anchor to lista, pozbywamy się znaków niedrukowalnych
        xdataa.append(anchor[0].strip())
    else:
        # trzeba pozbyć się znaków niedrukowalnych
        xdataa.append(header.text.strip())
arr = np.array(xdataa)
arr = np.reshape(arr, (100,7))
arr = np.delete(arr,[1,1], axis = 1)
labels = np.array(labels)
lab = []
for i in range(7):
    if labels[i] != '':
        lab.append(labels[i])
np.delete(lab,[1], axis = 0)
df = pd.DataFrame(arr, columns = lab)
df['Board Game Rank'] = np.arange(1,101)
df['Num Voters'] = pd.to_numeric(df['Num Voters'])
df.drop(['Shop'], axis = 1, inplace = True)

dff = df.sort_values(by=['Num Voters'], ascending = False)

dane = dff.head(10)
print(dane)
wykres = dane['Num Voters'].plot.bar()
wykres.set_xticklabels(dane['Title'])
plt.show()
