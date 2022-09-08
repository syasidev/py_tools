# zipcount-fileremove
# type : macro
# author : syasi

#import
import zipfile
import os

#parameter
target_dir = r"\\172.30.1.36\Videos2\Comics"

#define
def search(dir):
    if (len(os.listdir(dir)) == 0):
        os.rmdir(dir)
        return
    
    for name in os.listdir(dir):
        if(os.path.isdir(dir + "\\" + name)):
            search(dir + "\\" + name)
        else:
            if(name.endswith('.cbz')):
                run_process(name, dir)

def run_process(name, dir):
    fullname = dir+"\\"+name
    stories_zip = zipfile.ZipFile(fullname)
    
    print(fullname + "을 확인합니다 >> " + str(len(stories_zip.namelist())))
    if(len(stories_zip.namelist()) > 60):
        return
    
    print('삭제 >>> '+fullname)
    stories_zip.close()
    os.remove(fullname)
    
    if (os.path.exists(dir+"\\"+name[:-4]+".jpg")):
        print('삭제 >>> '+dir+"\\"+name[:-4]+".jpg")
        os.remove(dir+"\\"+name[:-4]+".jpg")
        
    if (os.path.exists(dir+"\\"+name[:-4]+".png")):
        print('삭제 >>> '+dir+"\\"+name[:-4]+".png")
        os.remove(dir+"\\"+name[:-4]+".png")
        
    if (os.path.exists(dir+"\\"+name[:-4]+".jpeg")):
        print('삭제 >>> '+dir+"\\"+name[:-4]+".jpeg")
        os.remove(dir+"\\"+name[:-4]+".jpeg")
        
    if (os.path.exists(dir+"\\"+name[:-4]+".gif")):
        print('삭제 >>> '+dir+"\\"+name[:-4]+".gif")
        os.remove(dir+"\\"+name[:-4]+".gif")

search(target_dir)
end = input()