import os,re, sys
content = ''
newfile = open(os.getcwd()+'\\'+'NCE3.txt','w')
path = os.getcwd()+'\\nce3\\'
for root,folder,files in os.walk(path):
	files.sort()
	for file in files:
		readF = open(os.getcwd()+'\\nce3\\'+file,'r').read()
		content = content +readF+'\n\n'
newfile.write(content)
newfile.close()
print 'done!'
		

