#change_kor
import os

def folder_check(name):
    return os.path.isdir(name)

def file_change(name, dir):
    index = name.find(".kor.")
    if(index > 1):
        return
    if name.endswith(".ass"):
       newName = name.replace(".ass", ".kor.ass")
       os.rename(dir+"\\"+name, dir+"\\"+newName)
       print(name + " >> 변환 >> " + newName)
    if name.endswith(".smi"):
       newName = name.replace(".smi", ".kor.smi")
       os.rename(dir+"\\"+name, dir+"\\"+newName)
       print(name + " >> 변환 >> " + newName)
    if name.endswith(".srt"):
       newName = name.replace(".srt", ".kor.srt")
       os.rename(dir+"\\"+name, dir+"\\"+newName)
       print(name + " >> 변환 >> " + newName)

def search(dir):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            search(dir + "\\" + name)
        else:
            file_change(name, dir)

#\\172.30.1.36\Videos
#search(r"\\172.30.1.36\Videos")
#\\172.30.1.36\Videos2
#search(r"\\172.30.1.36\Videos2")
#\\172.30.1.36\Videos3
#search(r"\\172.30.1.36\Videos3")

#search(r"\\172.30.1.36\Videos3\animation3\책벌레의 하극상 -사서가 되기 위해서라면 뭐든지 할 수 있어-")
search(r"\\172.30.1.36\Videos2\hentai")