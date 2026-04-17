"""
File: PotholeFilling.py
Name: TODO:謝元淏
--------------------------
任務:將圖片中的三個凹洞分別都填入99個beepers，且Karel結束的位置不能在凹洞裡
"""
from karel.stanfordkarel import *

#因為題目需要頻繁用到右轉、迴轉和放99個beepers，所以先定義這三個程式
def turn_right():
    for i in range(3):
        turn_left()
def turn_back():
    for i in range(2):
        turn_left()
def put_99_beepers():
    for i in range(99):
        put_beeper()
#將重複走的三次T字形定義成cycle，簡化主程式的步驟數
def cycle():
    move()
    turn_right()
    move()
    put_99_beepers()
    turn_back()
    move()
    turn_right()
    move()
#最後主程式再重複執行三次cycle就完成了
def main():
    for i in range(3):
        cycle()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
