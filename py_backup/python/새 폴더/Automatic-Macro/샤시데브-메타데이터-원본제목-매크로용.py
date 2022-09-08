#Syasi Py
#Macro :: 샤시데브 - 메타데이터 - 원본 제목 매크로용
import pyautogui
import time

x, y = pyautogui.position()
itemYpostion = y
count = 0
bigcount = 0

while bigcount < 10:
    print('bigcount ===> ' + str(bigcount))
    while count < 20:
        #아이템 선택
        clickYposition =  (count*32) + itemYpostion
        pyautogui.click(204, clickYposition)
        time.sleep(3)
        #경로 start (914,380)
        #경로 end   (1404,380)
        pyautogui.moveTo(914,380)
        pyautogui.mouseDown()
        pyautogui.moveTo(1854,380)
        pyautogui.mouseUp()
        pyautogui.hotkey('ctrl', 'c')
        #원본제목   (1025,555)
        pyautogui.click(1025,555)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        #저장       (2455,264)
        pyautogui.click(2455,264)
        print('count ===> ' + str(count))
        count = count + 1
        time.sleep(3)
    pyautogui.click(204, clickYposition)
    bigcount = bigcount + 1
    pyautogui.scroll(-768)
    count = 0

print('작업 완료')
end = input()

