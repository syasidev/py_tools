# file_name_replace
import os
dir = r"C:\Users\ghdus\Downloads\이 게임 폐인이 사는 법\새 폴더"

title = "이 게임 폐인이 사는 법"
season = "S01"
ext = "smi"
count = 1

for filename in os.listdir(dir):
    if(os.path.isdir(dir + "\\" + filename)):
        continue
    if(count < 10):
        new_filename = title + " - " + season + "E0" + str(count) + "." + ext;
    else:
        new_filename = title + " - " + season + "E" + str(count) + "." + ext;
    os.rename(dir + '\\' + filename, dir + '\\' + new_filename)
    count = count + 1;
    
    