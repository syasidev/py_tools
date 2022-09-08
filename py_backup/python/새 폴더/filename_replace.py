# file_name_replace
import os

for filename in os.listdir("."):
    if filename.endswith("jpg"):
        index = filename.lower().find(".mp4")
        new_filename = filename[0:index] + "-fanart.jpg"
        os.rename(filename, new_filename)