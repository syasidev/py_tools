from urllib.request import urlretrieve

path = 'C:\\Users\\ghdus\\Downloads\\[linda] 마조마마\\'
startNum = 157
endNum = 200
cateNum = '202'
convertName = ''

while startNum != endNum + 1:
    convertName = ''
    if startNum < 10:
        convertName = '00' + str(startNum)
    else:
        if startNum < 100:
            convertName = '0' + str(startNum)
        else:
            convertName = str(startNum)
    
    urlretrieve('https://manga.unknownpops.com/uploads/' + cateNum + '/' + str(startNum) + '.jpg', path + convertName + '.jpg')
    startNum = startNum + 1