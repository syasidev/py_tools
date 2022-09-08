#change_kor
import os

def folder_check(name):
    return os.path.isdir(name)

def file_change(name, dir):
    if(name.endswith('mkv') or name.endswith('mp4'))
    index = name.find(".kor.")
    if(index == -1):
        return
    print(name)

def search(dir):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            search(dir + "\\" + name)
        else:
            file_change(name, dir)

search(r"\\172.30.1.36\Videos3")
end = input()