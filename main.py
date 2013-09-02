#!/usr/bin/python

# main.py
#
# Main file for the game.

# Important imports
import random, os, sys, pygame, pdb
from pygame.locals import *

from game import *
from renderer import *

##############################################################################
# CONSTANTS
##############################################################################

# Screen resolution
SCREEN_X = 640
SCREEN_Y = 480

# Game frame rate
FPS = 15

def main():
    # Load a clock to limit the game FPS
    clock = pygame.time.Clock()

    pygame.init()

    # Initialize the sound mixer
    pygame.mixer.init()

    # Initialize the game main screen
    window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Students and Monobears')
    screen = pygame.display.get_surface()

    # Initialize a game
    game = Game()

    # DEBUG: Set entity locations
    #game.find_boat().location = 'left'
    game.find_student('Asahina').location = 'left'
    game.find_student('Kirigiri').location = 'left'
    #game.find_student('Fukawa').location = 'left'
    #game.find_monobear(0).location = 'left'
    game.find_monobear(1).location = 'left'
    #game.find_monobear(2).location = 'left'
    #game.board_boat(game.find_student('Kirigiri'))
    #game.board_boat(game.find_student('Asahina'))
    game.board_boat(game.find_student('Fukawa'))
    game.board_boat(game.find_monobear(0))
    #game.board_boat(game.find_monobear(1))
    #game.board_boat(game.find_monobear(2))
    game.move_boat()

    # Initialize a renderer for the graphics
    renderer = Renderer(game)

    # Main game loop
    while True:
        # Tick the game clock
        clock.tick(FPS)

        ######################################################################
        # GAME LOGIC
        ######################################################################

        # Something should go here
        
        ######################################################################
        # EVENT HANDLING
        ######################################################################

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)

        ######################################################################
        # DISPLAY UPDATES
        ######################################################################
        
        # Clear the screen
        renderer.clear_screen()

        # Draw the background image
        renderer.draw_background()

        # Draw the students
        renderer.draw_students()

        # Draw the monobears
        renderer.draw_monobears()

        # Draw the boat
        renderer.draw_boat()

        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
