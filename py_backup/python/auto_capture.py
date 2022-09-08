# -*- coding: utf-8 -*-
# file auto capture

import os
import cv2

rootdir = r"\\172.30.1.29\usb2\hen anime\Anime\バニラ\どんぶり家族"

for filename in os.listdir(rootdir):
    if filename.lower().endswith("mp4"):
        vidcap = cv2.VideoCapture(rootdir + "\\" + filename)
        count = 0
        index = filename.lower().find(".mp4")
        while(vidcap.isOpened()):
            ret, image = vidcap.read()
            
            #print(image)
            
            if(int(float(vidcap.get(1))) % 4000 == 0):
                address = rootdir+"\\"+filename[0:index]+"-"+str(count)+".png"
                print(address)
                cv2.imwrite(address, image)
                #print(rootdir)
                count += 1
                
                