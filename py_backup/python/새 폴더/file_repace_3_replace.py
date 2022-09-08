# file_name_replace
import os

dir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\####\windmill oasis"

for filename in os.listdir(dir):	
    print(filename)
    new_filename = filename.replace('[Windmill Oasis] ','')
    print(new_filename)
    os.rename(dir + '\\' + filename, dir + '\\' + new_filename)