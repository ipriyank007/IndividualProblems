from os import listdir
import os
from os.path import isfile, join

onlyfiles = [f for f in listdir(r'C:\Users\Priyank007\eclipse-workspace\GettingStarted\New Folder') if isfile(join(r'C:\Users\Priyank007\eclipse-workspace\GettingStarted\New Folder', f))]
print(onlyfiles)

def renameFile(name):
    print(name)
    dir = 'New Folder\\'
    tempname = dir + name
    finalname = tempname[:-4]
    os.rename(tempname, finalname)

for i in onlyfiles:
    renameFile(i)
print(onlyfiles)