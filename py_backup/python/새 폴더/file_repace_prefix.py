# file_name_prefix
import os

prefix = "6_"
rootdir = r"D:\hitomi_downloader_GUI\hitomi_downloaded\새 폴더"

for filename in os.listdir(rootdir):
    new_filename = prefix + filename
    os.rename(rootdir + "\\" + filename, rootdir + "\\" + new_filename)