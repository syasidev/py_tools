import zipfile
import os

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"
work_address = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"
endWith = ''
renameBefore = ''
renameNew = ''

for filename in os.listdir(rootdir):
    print(" >>> " + filename)
    if filename.endswith('.cbz'):
        stories_zip = zipfile.ZipFile(rootdir+"\\"+ filename)
        for file in stories_zip.namelist():
            stories_zip.extract(file, work_address)
            endWith = file[-4:]
            renameBefore = work_address + "\\" + file
            index = filename.lower().find(".cbz")
            renameNew = work_address + "\\" + filename[0:index] + endWith
            os.rename(renameBefore, renameNew)
            break

stories_zip.close()