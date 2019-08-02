# Bad character finder 1.0
# Written in python3
# Runs in linux/windows fine; currently tuned for evans debugger and immunity text files

import os
import re

charfile = str(input("Enter full path of bad character text file: "))
f = open(charfile,"r", errors='ignore') # open file charfile 'read', ignore encoding errors

debugChars = [] #list that will be populated with characters pulled from text file

for line in f.readlines():
    if "|" in line:
        line = line.replace("|"," ") #needed to break up lines pasted from edb
    for word in line.split():
        if len(word) < 4: # if not debugger garbage
            pattern = re.compile('\W')
            word = re.sub(pattern, '', word) #remove all non-alphanumeric characters
            if len(word) == 2: #if hex (probably)
                debugChars.append(word) #add hex char to debugChars list


compareList = [''] * 255 # empty list, will drop hex in appropriate list spots to compare against fullchar list
fullcharacters = [] # define list of all hex characters to check against
for x in range(1,256):
    fullcharacters.append('{:02x}'.format(x)) # populate full hex characters in list, 1-255

# iterate over range, use i to keep position of full characters list, and then drop it in appropriate position (i)
for i in range(1,256):
    try:
        for j in debugChars: # list of characters pulled from debugger text
            if fullcharacters[i].lower()==j.lower():
                compareList[i]=j.lower() # uses iter i as count to drop debugChars item into appropriate place
    except:
        pass # lazy

for i in range(1,256):
    try:
        if fullcharacters[i].lower() == compareList[i].lower():
            pass
        else:
            print(fullcharacters[i]," is missing")
    except:
        pass # still lazy
