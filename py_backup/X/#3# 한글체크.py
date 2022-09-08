import os
import time

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"

for filename in os.listdir(rootdir):
    print(" >>> " + filename)
    if filename.endswith('.cbz') or filename.endswith('.jpg'):
        newfilename = filename
        if filename.find(']') != -1:
            index = filename.rfind(']')
            if filename.find('｜') != -1:
                index2 = filename.find('｜') + 2
                text = filename[index+1:index2-1]
                newfilename = filename.replace(text, '')
            if filename.find('│') != -1:
                index2 = filename.find('│') + 2
                text = filename[index+1:index2-1]
                newfilename = filename.replace(text, '')
            if filename.find('｜') != -1:
                index2 = filename.find('｜') + 2
                text = filename[index+1:index2-1]
                newfilename = filename.replace(text, '')
            if filename.find('／') != -1:
                index2 = filename.find('／') + 2
                text = filename[index+1:index2-1]
                newfilename = filename.replace(text, '')
        os.rename(rootdir + '\\' + filename, rootdir + '\\' + newfilename)