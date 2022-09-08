import os

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"

for filename in os.listdir(rootdir):
    print(" >>> " + filename)
    if filename.endswith('.cbz'):
        newfilename = filename
        if filename.find('[') != -1:
            if filename.find('] ') != -1:
#                index = filename.find('] ') + 2
                index = filename.find(']')+1
                newfilename = filename[index:]
#        if filename.find('｜') != -1:
#            index = filename.find('｜') + 2
#            newfilename = filename[index:]
        os.rename(rootdir + '\\' + filename, rootdir + '\\' + newfilename)