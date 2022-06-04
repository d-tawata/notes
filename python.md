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