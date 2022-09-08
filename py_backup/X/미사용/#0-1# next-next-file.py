import os
import clipboard

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded"
rootdir2 = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"

first = ''
count = 0

for filename in os.listdir(rootdir):
    if filename.endswith('.cbz'):
        if count == 0:
            count = 1
        else:
            index = filename.find(']')
            index2 = filename.find(',')
            if index2 != -1:
                if index2 < index:
                    index = index2
            if first == '':
                first = filename[1:index]
                clipboard.copy('['+first+']')
            if filename[1:index] == first:
                os.rename(rootdir + '\\' + filename, rootdir2 + '\\' + filename)
