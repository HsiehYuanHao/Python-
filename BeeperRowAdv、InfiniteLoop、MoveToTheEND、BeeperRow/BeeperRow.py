"""
File: BeeperRow.py
Name:謝元淏
-------------------------
This program guides Karel to place beepers
along Street 1.

The goal of this program is to make Karel
fill the entire street with beepers in a
way that works for different world sizes,
not just one specific world.
"""

from karel.stanfordkarel import *

def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
