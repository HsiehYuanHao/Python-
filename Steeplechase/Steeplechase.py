"""
File: Steeplechase.py
Name: 謝元淏
---------------------------------
任務:跨欄，在最終牆壁(x=12.5)前停下
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()


def jump():
    """
    一開始面東，目標左轉後向東摸牆，摸不到牆則右轉後面東往前一格，再右轉面南向地面直走到底，最後左轉後回到面東狀態
    namely, pre: east
            post: east
    """
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
