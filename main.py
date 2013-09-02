#!/usr/bin/python

# main.py
#
# Main file for the game.

# Important imports
import random, os, sys, pygame, pdb
from pygame.locals import *

from game import *

##############################################################################
# CONSTANTS
##############################################################################

# Screen resolution
SCREEN_X = 640
SCREEN_Y = 480

# Game frame rate
FPS = 15

# Colors
WHITE = (255,255,255)

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

        # Clear the screen with white
        screen.fill(WHITE)

        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
