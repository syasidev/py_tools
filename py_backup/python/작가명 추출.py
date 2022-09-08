#작가명 추출
import os

a = []

def search(dir, dir2):
    for name in os.listdir(dir):
        if not name.endswith('.png') and not name.endswith('.jpeg') and not name.endswith('.jpg') and not name.endswith('.db'):
            index = name.find(']')
            a.append(name[1:index])
    for name in os.listdir(dir2):
        if not name.endswith('.png') and not name.endswith('.jpeg') and not name.endswith('.jpg') and not name.endswith('.db'):
            index2 = name.find(']')
            if not name[1:index2] not in a:
                a.remove(name[1:index2])
    print('\n'.join(a))



#search(r"\\172.30.1.36\Videos2\Comics\X", r"\\172.30.1.36\Videos2\doujinshi\X")
#search(r"\\172.30.1.36\Videos2\Comics\Y", r"\\172.30.1.36\Videos2\doujinshi\Y")
search(r"\\172.30.1.36\Videos2\Comics\Z", r"\\172.30.1.36\Videos2\doujinshi\Z")
end = input()