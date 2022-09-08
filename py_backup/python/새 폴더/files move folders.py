# files move folders.py
# author : syasi
# 
# 'XX'라는 폴더에서 'YY'라는 폴더로 이동시킬때 사용합니다.
# 두 폴더간 '같은 파일명'을 찾아서 있는 경우, 'YY'의 해당 파일을 지우고 'XX'에 있는 파일로 대체시킵니다.
# 타겟이 되는 폴더는 하위폴더까지 탐색범위를 늘릴 수 있으며, 특정확장자를 지정하여 작업속도를 빠르게 할 수 있습니다.
# 하위폴더를 활용하는 경우 하위폴더내에 같은 파일명이 복수로 존재하는 경우 해당 프로그램을 사용하지 마십시오.
# 이 프로그램은 목록화하여 진행하지 않습니다.

import os
import shutil

#소스가 될 폴더 < 해당 주소의 파일들이 이동에 사용됩니다 >
source_folder = r"C:\Users\ghdus\Desktop\setting\작업중\### 작업완료"
#타겟 폴더 < 대상의 주소이며 해당 폴더에 파일들이 변경됩니다 > 
target_folder = r"\\172.30.1.36\Videos2\Comics"
#타켓 폴더의 하위폴더를 활용할지 여부
use_deep = True
#확장자 체크
use_endsWith = True
#확장자 지정 < 확장자 체크를 하는 경우 지정하십시오 >
target_endswith = ".cbz"
#드라이브간 이동여부 < 드라이브 및 타시스템간 이동하는 경우 해당 부분을 체크하십시오 >
use_other_drive = True

# 폴더인지 체크
def folder_check(name):
    return os.path.isdir(name)

# 디렉토리 
def search(dir):
    for name in os.listdir(dir):
        if(folder_check(dir + "\\" + name)):
            if(use_deep):
                search(dir + "\\" + name)
        else:
            if(use_endsWith):
                if(name.endswith(target_endswith)):
                    item_check(name, dir)
            else:
                item_check(name, dir)

# 항목 여부 확인
def item_check(name, dir):
    for source_name in os.listdir(source_folder):
        if(source_name == name):
            change_file(name, dir)

# 파일삭제
def delete_file(name, dir):
    path_name = dir + "\\" + name
    #print("delete_file >> " + path_name)
    if(os.path.exists(path_name)):
        os.remove(path_name)
        print("[info] 파일을 삭제했습니다 >>> " + path_name)
    else:
        print("[error] 파일이 존재하지 않습니다")

# 파일이동 dir -> dir2
def move_file(name, dir, dir2):
    source_path = dir + "\\" + name
    target_path = dir2 + "\\" + name
    if(os.path.exists(target_path)):
        print("[error] 파일이 존재하여 이동되지 않았습니다")
    else:
        if(use_other_drive):
            shutil.move(source_path, target_path)
        else:
            os.rename(source_path, target_path)
        print("[info] 파일을 이동했습니다 >>> " + target_path)

# 변경작업 실시
def change_file(name, dir):
    print("===========================================================")
    print("[info] 일치하는 데이터를 찾았습니다. >>> " + name)
    delete_file(name, dir)
    move_file(name, source_folder, dir)

# start
print("작업이 시작됩니다")
search(target_folder)
print("=== 뽜밤뽜밤 작업이 완료되었습니다 ^^ ===")
end = input()