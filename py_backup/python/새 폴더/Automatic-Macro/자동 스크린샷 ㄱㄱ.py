#Syasi Py
#Macro :: 샤시데브 - 메타데이터 - 원본 제목 매크로용
import pyautogui
import time

count = 1

print('시작합니다')
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)

while count < 10000:
    print(str(count) + '회 작업중')
    pyautogui.hotkey('alt', 'printscreen')
    pyautogui.hotkey('alt', 'printscreen')
    pyautogui.hotkey('alt', 'printscreen')
    time.sleep(0.41)
    pyautogui.hotkey('alt', 'home')
    pyautogui.press('up')
    time.sleep(0.75)
    count = count + 1
    
end = input()