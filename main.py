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

    # Initialize the sound mixer
    pygame.mixer.init()

    # Initialize the game main screen
    window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Students and Monobears')
    screen = pygame.display.get_surface()

    # Initialize a game
    game = Game()

    # DEBUG: Set boat location
    #game.find_boat().location = 'left'

    # Initialize a renderer for the graphics
    renderer = Renderer()

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

        # Draw the boat
        renderer.draw_boat(game.find_boat().location)

        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
