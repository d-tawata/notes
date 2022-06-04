import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url) # get copy of website's html document
soup = BeautifulSoup(response.text, 'lxml') # parse html document, using lxml parser
#print(soup) # html output
quotes = soup.find_all('span', class_='text') # find quote information
authors = soup.find_all('small', class_='author') # find author information
tags = soup.find_all('div', class_='tags') # find tag information (multiple tags per quote)

print(tags)
# version 1
# count = 0
# for quote in quotes:
#     print(quote.text + '\n' + authors[count].text)
#     count = count + 1

# version 2
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)