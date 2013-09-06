#!/usr/bin/python

# clitest.py
#
# Program to test the game without resorting to pygame graphics.
import pdb, sys, os

from game import Game
from entity import Entity
from monobear import Monobear
from student import Student
from ai_solver import *

def ai_test():
    game = Game()
    ai = AI(game)
    # Get the AI to find a path
    ai.solve()
    while True:
        #os.system('clear')

        if game.check_if_won():
            print('AI is done!')
            game.display_statistics()
            return True
        if game.check_if_lost():
            print('AI encountered an error')
            game.display_statistics()
            return False
        # Display game statistics
        game.display_statistics()

        # Display the path
        print('Path')
        for node in ai.path:
            node.print_node()
        print('End of path list')

        # Get the AI to make their move
        ai.make_move(ai.path.pop(1))

        # Display game statistics
        game.display_statistics()

        a = raw_input('Press any key to continue >')

def play_test():
    game = Game()
    while True:
        os.system('clear')

        if game.check_if_won():
            print('You won!')
            game.display_statistics()
            return True
        if game.check_if_lost():
            print('You lost!')
            game.display_statistics()
            return False

        # Display game status
        game.display_statistics()

        print('\nOptions:')
        print('[a] Move boat ')
        if(not (game.find_boat().check_full()) and
                len(game.get_potential_passengers_on_side(
                game.find_boat().location))):
            print('[b] Board boat')
        if(len(game.find_boat().passengers)):
            print('[c] Disembark from boat')
        input = raw_input('Your choice > ')
        input.lower()

        if input is 'a':
            game.move_boat()
        elif(input is 'b' and not game.find_boat().check_full() and
                len(game.get_potential_passengers_on_side(
                game.find_boat().location))):
            print('Who should board the boat?')
            # Get a list of potential passengers
            potentials = game.get_potential_passengers_on_side(
                    game.find_boat().location)
            x = 0
            for entity in potentials:
                print('[' + str(x) + ']')
                game.print_entity_information(entity)
                x += 1
            input = raw_input('Your choice > ')
            game.board_boat(potentials[int(input)])
        elif(input is 'c' and len(game.find_boat().passengers)):
            print('Who should get off the boat?')
            x = 0
            for passenger in game.find_boat().passengers:
                print('[' + str(x) + ']')
                game.print_entity_information(entity)
                x += 1
            input = raw_input('Your choice > ')
            game.disembark_boat(game.find_boat().passengers[int(input)])

def main():
    print('Students and Monobears CLI test')
    input = raw_input('[a] Play test [b] AI Testing [c] Quit -> ')
    input.lower()
    if input is 'a':
        print('Play testing initialized')
        if(play_test()):
            print('You have won')
        else:
            print('You have lost!')
    elif input is 'b':
        print('AI testing initialized')
        if(ai_test()):
            print('You have won')
        else:
            print('You have lost!')
    else:
        return 0

if __name__ == '__main__':
    main()
