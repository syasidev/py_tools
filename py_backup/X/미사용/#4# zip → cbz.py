import os

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"

for filename in os.listdir(rootdir):
    print(" >>> " + filename)
    if filename.endswith('.zip'):
        newfilename = filename.replace('.zip', '.cbz')
        os.rename(rootdir + '\\' + filename, rootdir + '\\' + newfilename)