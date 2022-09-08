# directory report
import os

data = ""

def folder_check(name):
    return os.path.isdir(name)

def print_dir(name, dir, i):
    while(i>0):
        data = data + " "
        i = i-1
    data = data + name + "\r\n")

def search(dir, i):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            search(dir + "\\" + name, i+4)
        else:
            print_dir(name, dir, i)

def start(dir):
    f = open("report.txt", 'w')
    search(dir, 0)
    f.write(data)
    f.close()


start(r"\\172.30.1.36\Videos2\Comics\H")