### Using Python for Automation (LinkedIn Learning)
#### 1. Automate File, Folder, and Terminal Interactions
##### How to read files
```python
f = open('inputFile.txt', 'r') # 'r' for reading file
print(f.read())
f.close() # remember to close!
```
Only print lines tagged at the end with 'P':
```python
f = open('inputFile.txt', 'r')  # 'r' for reading file
count = 0
for line in f:
    line_split = line.split() # splits string by white spaces
    if line_split[2] == 'P':
        print(line_split[0] + " " + line_split[1])
    #print(str(count) + line)
    count = count + 1
f.close()  # remember to close!
```
##### How to write files
```python
f = open('inputFile.txt', 'r')  # 'r' for reading file
# creates new file, 'w' to write to this file
passFile = open('PassFile.txt', 'w')  # stores names that pass
failFile = open('FailFile.txt', 'w')  # stores names that fail
count = 0
for line in f:
    line_split = line.split()  # splits string by white spaces
    if line_split[2] == 'P':
        passFile.write(line)  # writes onto file
    else:
        failFile.write(line)
    count = count + 1
f.close()  # remember to close!
passFile.close()
failFile.close()
```
##### Executing terminal commands
example.py
```python
print("Hello World")
```
script.py
```python
import subprocess
for i in range(0,5):
    subprocess.check_call(['python3','example.py']) # run command with arguments
```
Output:
```python
Hello World
Hello World
Hello World
Hello World
Hello World
```
##### Organizing directories
organize.py (Make sure you and this file are in the directory you wish to scan)
```python
import os
from pathlib import Path
# dictionary (keys: values)
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','jpeg','.png']
}
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items(): # goes through keys and values
        for suffix in suffixes: # goes through the values for a single key
            if suffix == value: # if the argument matches a value in the dictionary, returns the key / category
                return category
    return 'MISC' # if the file type does not match any value in the dictionary
#print(pickDirectory('.avi'))
def organizeDirectory():
    for item in os.scandir(): # goes through each item in the directory / folder
        # skips if item is a directory
        if item.is_dir():
            continue
        filePath = Path(item) # get the file path for each item
        fileType = filePath.suffix.lower() # .suffix returns the file extension
        directory = pickDirectory(fileType) # get the category for this file type
        directoryPath = Path(directory) # cast the category to a path
        if directoryPath.is_dir() != True: # if the directory does not exist
            directoryPath.mkdir() # make the directory
        filePath.rename(directoryPath.joinpath(filePath)) # move file into directory

organizeDirectory()
```
#### 2. Web Scraping with Beautiful Soup
##### The value of web scraping
###### Libraries
- Beautiful Soup: used to create a parsed and navigable html document
- lxml: used for processing html
- requests: used for creating the 'get' query

###### Install Packages
1. Open Terminal
2. Use your package installer to install each (pip3 install *library*)
   1. requests
   2. lxml
   3. beautifulsoup4

##### Creating a request and parsing
scrape.py
```python
import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url) # get copy of website's html document
soup = BeautifulSoup(response.text, 'lxml') # parse html document, using lxml parser
print(soup) # html output
```

##### How to isolate data
```python
import requests
from bs4 import BeautifulSoup
url = 'https://quotes.toscrape.com/'
response = requests.get(url) # get copy of website's html document
soup = BeautifulSoup(response.text, 'lxml') # parse html document, using lxml parser
quotes = soup.find_all('span', class_='text') # find quote information
authors = soup.find_all('small', class_='author') # find author information
tags = soup.find_all('div', class_='tags') # find tag information (multiple tags per quote)

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
```

##### Scraping paginated content
scrapePages.py
```python
from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for i in items:
    itemName = i.find('h4', class_='card-title').text.strip('\n') # .strip gets rid of new line
    itemPrice = i.find('h5').text
    print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
    count = count + 1
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None # None if text is not a number
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
for i in urls:
    newUrl = url + i
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_='card-title').text.strip('\n') # .strip gets rid of new line
        itemPrice = i.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (count, itemPrice, itemName))
        count = count + 1
```
#### 3. Automate Web Browsing with Selenium
##### Automating web browsing
###### Why automate browsing?
- **Test Website Functionality**
  - Decreases cost and time
  - Provides round the clock testing
  - Makes cross-browser proofing easier
- **Botting Processes**
  - botting: a piece of software that executes commands or performns routine tasks without user intervention
  - script any repetitive tasks
  - filling out forms
  - logging in

Any repetitive online task can be optimized with a Python script.

##### Basic browser interactions

Copy XPath (element-specific) from inspector in website.

webBrowse.py
```python
from selenium import webdriver
driver = webdriver.Firefox() # initialize webdriver
driver.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# single input field
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World') # inputs message into text box
showMessageButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

# two input fields
fieldA = driver.find_element_by_xpath('//*[@id="sum1"]')
fieldA.send_keys('5')
fieldB = driver.find_element_by_xpath('//*[@id="sum2"]')
fieldB.send_keys('12')
getTotalButton = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotalButton.click()
```

##### Handling drag and drop