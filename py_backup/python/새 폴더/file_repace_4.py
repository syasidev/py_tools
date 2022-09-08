# file_name_replace
import os

alphabet = "Z"

def start(name):
    rootdir = r'\\172.30.1.36\Videos2\Comics\[' + alphabet + ']'
    os.rename(rootdir + '\\' + name, rootdir + '\\[' + name + ']')
    dir = rootdir + '\\[' + name + ']'
    for filename in os.listdir(dir):	
        print(filename)
        new_filename = filename.replace('['+name+'] ','')
        new_filename = new_filename.replace('['+name+', Etc] ','')
        print(new_filename)
        os.rename(dir + '\\' + filename, dir + '\\' + new_filename)
        
        
#              ['AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA']
#name_list = ['AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA']
#name_list = ['Nagare Ippon','Namamo Nanase','Namboku','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA','AAAAAAA']


#for name in name_list:
#    start(name)

rootddir = r"\\172.30.1.36\Videos2\Comics\[" + alphabet + "]"
for xname in os.listdir(rootddir):
    if os.path.isdir(rootddir+"\\"+xname):
        if (xname.find("[") < 0):
            start(xname)    