"""
File: BeeperRowAdv.py
Name:謝元淏
------------------------------
任務:在封閉的一條路上行走，走到末端時路上的每格都只能有一個beeper，而這樣的程式碼要能在每個程式世界都達成任務
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)