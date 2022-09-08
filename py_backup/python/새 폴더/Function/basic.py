# basic.py
# author : syasi

# 문자열 출력
print("hello world")

# Substring
text = "hello world"
print("text[2:10] >> " + text[2:10])
# llo worl
print("text[:-4] >> " + text[:-4])
# hello w [ 3자리 확장자 제거에 사용 ]

# def = 함수 정의
def show():
    print(text)

show()

# class 샘플
class TextGenerator:
    def __init__(self):
        print("make TextGenerator")
    
    def show_print(self,text):
        print(text)

c = TextGenerator()
c.show_print("new world")