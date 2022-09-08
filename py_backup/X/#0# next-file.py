import os
import clipboard
import time

rootdir = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded"
rootdir2 = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X"
rootdir3 = r"C:\Users\ghdus\Desktop\setting\hitomi_downloader\hitomi_downloaded\X\# completed"

first = ''

flag = 0
subdir = ''
datalength = 0

for filename in os.listdir(rootdir2):
    if filename.endswith('.cbz'):
        flag = 1

if flag == 1:
    for filename in os.listdir(rootdir2):
        if filename.startswith('[') and filename.endswith(']'):
            subdir = filename
            flag = 2

if flag == 2:
    for filename in os.listdir(rootdir2):
        if filename.endswith('.cbz') or filename.endswith('.jpg'):
            os.rename(rootdir2 + '\\' + filename, rootdir2 + '\\' + subdir + '\\' + filename)
    flag = 3

for filename in os.listdir(rootdir):
    if filename.endswith('.cbz'):
        index = filename.find(']')
        index2 = filename.find(',')
        if index2 != -1:
            if index2 < index:
                index = index2
        if first == '':
            first = filename[1:index]
            clipboard.copy('['+first+']')
        if filename[1:index] == first:
            os.rename(rootdir + '\\' + filename, rootdir2 + '\\' + filename)
            datalength = datalength + 1

if first != '':
    if datalength > 1: 
        os.makedirs(rootdir2 + '\\' + '[' + first + ']')
        exec(open(rootdir2 + '\\' + '#1# 작가명 컷팅.py', "r", encoding="utf8").read())
        exec(open(rootdir2 + '\\' + '#2# 시리즈변환.py', "r", encoding="utf8").read())
        exec(open(rootdir2 + '\\' + '#3# 한글체크.py', "r", encoding="utf8").read())
        exec(open(rootdir2 + '\\' + '#5# unzip_first.py', "r", encoding="utf8").read())
    else:
        exec(open(rootdir2 + '\\' + '#2# 시리즈변환.py', "r", encoding="utf8").read())
        exec(open(rootdir2 + '\\' + '#3# 한글체크.py', "r", encoding="utf8").read())
        exec(open(rootdir2 + '\\' + '#5# unzip_first.py', "r", encoding="utf8").read())
#        exec(open(rootdir2 + '\\' + '#6# 파일이동.py', "r", encoding="utf8").read())
        for filename in os.listdir(rootdir2):
            if filename.endswith('.cbz') or filename.endswith('.jpg'):
                os.rename(rootdir2 + '\\' + filename, rootdir2 + '\\# completed\\' + filename)
        exec(open(rootdir2 + '\\' + '#0# next-file.py', "r", encoding="utf8").read())