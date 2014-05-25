import os,re

rawFolderL=[]
rawFileL=[]
for a,b,c in os.walk(os.getcwd()):
    rawFolderL.append(b)
    rawFileL.append(c)

rFolders = []
for folder in rawFolderL[0]:
    if '_' in folder.split('.')[0]:
        folderName = folder.split('.')[0].split('_')[0]
    else:
        folderName = folder.split('.')[0]
    rFolders.append(folderName)
        
rFiles = []     
for file in rawFileL[0]:
    if '_' in file:
        fileName = file.split('_')[0]
    else:
        fileName = file.split('.')[0]
    rFiles.append(fileName)
    
print rFolders
print rFiles

for f in rFolders:
    if f not in rFiles:
        rawFolder = rawFolderL[0][rFolders.index(f)]
        print 'the raw folder is '+rawFolder
        os.removedirs(rawFolder)