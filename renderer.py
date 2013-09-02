# renderer.py
#
# Python file containing the source for rendering the graphics and images
# required for the game.

import pygame, os, sys
from pygame.locals import *

# Screen resolution
SCREEN_X = 640
SCREEN_Y = 480

# Colors
WHITE = (255,255,255)

class Renderer():
    def draw_background(self):
        """
        Draws the background image onto the screen.
        """
        screen = pygame.display.get_surface()

        # Load the background image
        bg_image = pygame.image.load(os.path.join("images", "bg.png"))

        # Blit the background image onto the screen
        screen.blit(bg_image, (0,0))

    def clear_screen(self):
        """
        Clears the screen by filling it with white
        """
        screen = pygame.display.get_surface()
        screen.fill(WHITE)

    def highlight_rect(self, rect, color=(255,0,0), width=0):
        """
        Highlights the given rect with the optional color argument
        """
        screen = pygame.display.get_surface()

        pygame.draw.rect(screen, color, rect, width)

    def draw_boat(self, location):
        """
        Draws the boat onto the screen depending on the given location.
        """
        screen = pygame.display.get_surface()

        # Load the boat image
        boat_image = pygame.image.load(os.path.join("images", "boat.png"))

        # Scale the image to half
        boat_image = pygame.transform.scale(boat_image,
                ((boat_image.get_rect().width / 5),
                (boat_image.get_rect().height / 5)))

        # Get the coordinates where we should put the boat in
        if location is 'right':
            boat_pixel_loc = ((SCREEN_X - 180) -
                    boat_image.get_rect().width, (SCREEN_Y / 2) -
                    (boat_image.get_rect().height / 2))
        else:
            boat_pixel_loc = (180, (SCREEN_Y / 2) -
                    (boat_image.get_rect().height / 2))

        boat_image.get_rect().topleft = boat_pixel_loc
        #self.highlight_rect(boat_image.get_rect(), (255,0,0), 1)

        # Blit the boat to that location
        screen.blit(boat_image, boat_pixel_loc)
