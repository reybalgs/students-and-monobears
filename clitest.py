#!/usr/bin/python

# clitest.py
#
# Program to test the game without resorting to pygame graphics.

from game import Game

def main():
    print('Students and Monobears CLI test')
    input = raw_input('[a] Play test [b] AI Testing [c] Quit -> ')
    input.lower()
    if input is 'a':
        print('Play testing initialized')
    elif input is 'b':
        print('AI testing not yet implemented')
    else:
        return 0

if __name__ == '__main__':
    main()
