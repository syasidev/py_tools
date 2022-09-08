import os
import time

rootdir2 = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"

for filename in os.listdir(rootdir2):
    if filename.endswith('.cbz') or filename.endswith('.jpg'):
        print('filename as : ' + rootdir2 + '\\' + filename)
        print('filename to : ' + rootdir2 + '\\# completed\\' + filename)
        os.rename(rootdir2 + '\\' + filename, rootdir2 + '\\# completed\\' + filename)