# Unzip-ImageResize-zip
# type : macro
# author : syasi

#import
import zipfile
import os
from PIL import Image

#parameter
target_dir = r"C:\Users\ghdus\Desktop\setting\작업중\#### 작업중"
target_size = 480

#define
def search(dir):
    for name in os.listdir(dir):
        if(os.path.isdir(dir + "\\" + name)):
            search(dir + "\\" + name)
        else:
            if(name.endswith('.zip')):
                print('작업시작 >>> '+name)
                run_process(name, dir)

def run_process(name, dir):
    #존재 여부 확인
    if(os.path.isdir(dir + "\\" + name)):
        return
    
    #압축해제
    stories_zip = zipfile.ZipFile(dir+"\\"+ name)
    for file in stories_zip.namelist():
        stories_zip.extract(file, dir+"\\"+name[:-4])
        #리사이즈
        resizing(file,dir+"\\"+name[:-4])
    stories_zip.close()
        
    #기존 압축파일 삭제
    os.remove(dir+"\\"+name)
    
    #새로 압축
    new_zip = zipfile.ZipFile(dir+"\\"+name[:-4]+".zip", 'w')
    for folder, subfolders, files in os.walk(dir+"\\"+name[:-4]):
        for file in files:
            new_zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)
    new_zip.close()
    
    #이미지 삭제
    for file in os.listdir(dir+"\\"+name[:-4]):
        os.remove(dir+"\\"+name[:-4]+"\\"+file)
    
    # 디렉토리 삭제
    os.rmdir(dir+"\\"+name[:-4])

def resizing(name,dir):
    path = dir + "\\" + name
    
    if(not (path.endswith(".gif") or path.endswith(".jpg") or path.endswith(".jpeg") or path.endswith(".bmp") or path.endswith(".png"))):
        return
    
    try:
        img = Image.open(path)
        max_size = 0
        
        if(img.width > img.height):
            max_size = img.width
        else:
            max_size = img.height
        
        if(max_size > target_size):
            rato = max_size / target_size
            img_resize = img.resize((int(img.width / rato), int(img.height / rato)))
            img_resize.save(path)
            #print("이미지 변환완료 >> " + path)
    except:
        img.close()
        print("잘못된 이미지 파일을 발견했습니다. 삭제합니다! : " + name)
        os.remove(path)

#run
print(" == 작업이 시작됩니다 == ")
search(target_dir)
print(" == 뽜밤뽜밤 작업이 완료됐습니다 ^^ == ")
end = input()