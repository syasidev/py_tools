# 정리 프로그램을 만들자ㅏㅏㅏㅏ
import os

dir = r"\\172.30.1.36\Videos2\Comics\[K]"
fileList = []
AuthList = []
dotPosi = None
endPosi = None
lastPosi = None

for filename in os.listdir(dir):
    if(os.path.isdir(dir + "\\" + filename)):
        continue
    fileList.append(filename)

for file in fileList:
    dotPosi = file.find(',')
    endPosi = file.find(']')
    if(dotPosi == -1):
        lastPosi = endPosi
    else:
        lastPosi = dotPosi
    
    AuthList.append(file[1:lastPosi])

for auth in AuthList:
    print(auth)