# image resize
# author : syasi
#
# 이미지 파일을 찾아서 리사이즈 합니다
# 기타 자세한 내용은 하기 옵션을 참조
import os
from PIL import Image

##############Options
# 대상폴더
target_folder = r"C:\Users\ghdus\Desktop\setting\작업중\#### 작업중"
# 타켓 폴더의 하위폴더를 활용할지 여부
use_deep = True
# 품질 < NEAREST, BOX, BILINEAR, HAMMING, BICUBIC, LANCZOS > <<- 우측으로 갈 수록 고품질 (ex : Image.LANCZOS)
#quality = Image.LANCZOS

## 긴축을 기준으로 지정된 값의 비율만큼 리사이즈 작업을 실시합니다
#
# ex) 1400 x 700인 파일의 경우 긴축은 1400 입니다. 지정된 값이 1024 일때,
# 1400 / x = 1024  ==> x = 1.3671875 이므로, 1400 x 700 은 해당 사이즈가 됩니다. ==> 1024 x 957
target_size = 1024


# 폴더 체크
def folder_check(name):
    return os.path.isdir(name)

# 디렉토리
def search(dir):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            if(use_deep):
                search(dir + "\\" + name)
        else:
            if(name.endswith('.jpg') or name.endswith('.png') or name.endswith('.gif') or name.endswith('.jpeg')):
                testkg(name, dir)

# 리사이즈 작업
def testkg(name,dir):
    path = dir + "\\" + name
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
        #os.remove(path)
        print("변환완료 >> " + path)

print("작업이 시작됩니다")
search(target_folder)
print("=== 뽜밤뽜밤 작업이 완료되었습니다 ^^ ===")
end = input()