# file_name_replace
import os

#name = "Sansyoku Amido."
dir = r"D:\hitomi_downloader_GUI\hitomi_downloaded"

for filename in os.listdir(dir):	
    print(filename)
    #new_filename = filename.replace('['+name+'] ','')
    new_filename = filename.replace('[Henreader] ','')
    print(new_filename)
    os.rename(dir + '\\' + filename, dir + '\\' + new_filename)