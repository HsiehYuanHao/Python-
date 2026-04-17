"""
File: MoveToTheEnd.py
Name:謝元淏
------------------------
This program demonstrates how to use a
while loop to move Karel to the end of
a row in the Karel world.

By checking whether the front is clear,
Karel will keep moving forward until it
reaches the end of the row.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end of the first Street in any world
    """
    pass
    while front_is_clear():
        move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
