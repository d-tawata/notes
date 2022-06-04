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