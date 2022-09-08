#file_tree_view_move
import os
import shutil

rootdir = r"\\172.30.1.29\usb2\hen anime\Anime\魔人"

def search_dir(dir):
    for filename in os.listdir(dir):
        if filename == "@eaDir":
            continue
        file_full_name = dir + "\\" + filename
        if os.path.isdir(file_full_name):
            search_dir(file_full_name)
        else:
            if filename.lower().endswith('.mp4'):
                for filename2 in os.listdir(r"D:\PotPlayer\Capture"):
                    index = filename.lower().find(".mp4")
                    if filename[0:index] == filename2[0:index]:
                        shutil.move(r"D:\PotPlayer\Capture" + "\\" + filename2[0:index] + "-fanart.jpg", dir + "\\" + filename2[0:index] + "-fanart.jpg")
                        print(dir + filename2[0:index] + "-fanart.jpg")



search_dir(rootdir)