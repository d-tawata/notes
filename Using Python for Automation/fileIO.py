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
