#Syasi Py
#Macro :: 좀더 쉽게 일을 하자
import pyautogui
import time

while 1 == 1:
    k = input()
    if k == str(1):
        print('start')
        ##pyautogui.moveTo(2067,545)
        pyautogui.click(2067,545)
        time.sleep(2)
        
        pyautogui.click(437,160)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        
        pyautogui.click(723, 109)
        time.sleep(2)
        #pyautogui.click(x=2067,y=545)
        #pyautogui.hotkey('ctrl', 'shift', 'p')
        #time.sleep(1)clicks=3, interval=1
        #pyautogui.move(x=437,y=160)
        #pyautogui.click(x=437,y=160)
        #pyautogui.hotkey('ctrl', 'a')
        #pyautogui.hotkey('ctrl', 'v')
        #pyautogui.move(x=723,y=109)
        #pyautogui.click(x=723,y=109)