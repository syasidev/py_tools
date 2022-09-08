#이름 변환
import os

def folder_check(name):
    return os.path.isdir(name)

def file_change(name, dir):
    index = name.find('-S0')
    if(index > 1):
        newName = name.replace("-S0", " S0")
        print(name + " >> 변환 >> " + newName)
        os.rename(dir+"\\"+name, dir+"\\"+newName)
    index = name.find(' - S0')
    if(index > 1):
        newName = name.replace(" - S0", " S0")
        print(name + " >> 변환 >> " + newName)
        os.rename(dir+"\\"+name, dir+"\\"+newName)

def search(dir):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            search(dir + "\\" + name)
        else:
            file_change(name, dir)

#search(r"\\172.30.1.36\Videos\animation")
#search(r"\\172.30.1.36\Videos3\animation3")
search(r"\\172.30.1.36\Videos3\animation3 - 진행중")