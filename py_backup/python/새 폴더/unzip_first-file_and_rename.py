import zipfile
import os

rootdir = r"D:\hitomi_downloader_GUI\hitomi_downloaded"
work_address = r"D:\data\[0] WORK FOLDER [0]"
endWith = ''
renameBefore = ''
renameNew = ''

for filename in os.listdir(rootdir):
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