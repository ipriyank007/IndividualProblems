import pandas as pd
from os import listdir
import os
from os.path import isfile, join
filenames = []
onlyfiles = [f for f in listdir(r'C:\Users\Evolet\PycharmProjects\FormTask\New folder') if isfile(join(r'C:\Users\Evolet\PycharmProjects\FormTask\New folder', f))]
print(onlyfiles)

def renameFile(name):
    global filenames
    dir = 'New folder\\'
    tempname = dir + name
    finalname = tempname[:-4]
    os.rename(tempname, finalname)
    print(finalname)
    filenames.append(finalname)
def deleteFiles(fileToDelete):
    os.remove(fileToDelete)

for i in onlyfiles:
    renameFile(i)
print(onlyfiles)

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined_csv.to_csv( filenames[0], index=False )

for i in filenames[1:]:
    deleteFiles(i)
