# renderer.py
#
# Python file containing the source for rendering the graphics and images
# required for the game.

import pygame, os, sys
from pygame.locals import *

from student import Student
from boat import Boat
from monobear import Monobear

# Screen resolution
SCREEN_X = 640
SCREEN_Y = 480

# Colors
WHITE = (255,255,255)

# Coordinates
X = 0
Y = 1

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

    def draw_monobears(self):
        """
        Draws the monobears onto the screen, using the lsit of monobears as a
        reference.
        """
        screen = pygame.display.get_surface()

        # Clear the monobear rects
        self.monobear_rects = []
        # Get the locations of the monobears
        monobear_locations = self.game.return_monobear_locations()
        print('Monobear locations: ' + str(monobear_locations))
        # Load the boat
        boat = self.game.find_boat()
        # Load the boat topleft location
        boat_topleft = self.find_boat_topleft()

        # Load the Monobear image
        monobear_image = pygame.image.load(os.path.join("images",
            "monobear.png"))
        # Resize the monobear image
        monobear_image = pygame.transform.scale(monobear_image,
                (monobear_image.get_rect().width / 10,
                monobear_image.get_rect().height / 10))

        # Set the locations of the monobears
        x = 0
        while x < 3:
            location = monobear_locations[x]
            if x == 0:
                # First monobear
                if location is 'left':
                    # The monobear is on the left
                    monobear_location = (0, (SCREEN_Y / 2))
                elif location is 'right':
                    # The monobear is on the right
                    monobear_location = ((SCREEN_X - 180), (SCREEN_Y / 2))
                elif location is 'boat':
                    # The monobear is on the boat
                    # Get the position of the monobear on the boat
                    position = 0
                    for passenger in boat.passengers:
                        if isinstance(passenger, Monobear):
                            if passenger.number is x:
                                break
                        position += 1
                    if position:
                        monobear_location = (boat_topleft[X] + 56,
                                boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
                    else:
                        monobear_location = (boat_topleft[X], boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
            elif x == 1:
                # Second monobear
                if location is 'left':
                    # The monobear is on the left
                    monobear_location = (monobear_image.get_rect().width,
                            (SCREEN_Y / 2))
                elif location is 'right':
                    # The monobear is on the right
                    monobear_location = ((SCREEN_X - 180) +
                            monobear_image.get_rect().width, (SCREEN_Y / 2))
                elif location is 'boat':
                    # The monobear is on the boat
                    position = 0
                    for passenger in boat.passengers:
                        if isinstance(passenger, Monobear):
                            if passenger.number is x:
                                break
                        position += 1
                    if position:
                        monobear_location = (boat_topleft[X] + 56,
                                boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
                    else:
                        monobear_location = (boat_topleft[X], boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
            elif x == 2:
                # Third monobear
                if location is 'left':
                    # The monobear is on the left
                    monobear_location = (monobear_image.get_rect().width * 2,
                            (SCREEN_Y / 2))
                elif location is 'right':
                    # The monobear is on the right
                    monobear_location = ((SCREEN_X - 180) +
                            (monobear_image.get_rect().width +
                            monobear_image.get_rect().width), (SCREEN_Y / 2))
                elif location is 'boat':
                    # The monobear is on the boat
                    position = 0
                    for passenger in boat.passengers:
                        if isinstance(passenger, Monobear):
                            if passenger.number is x:
                                break
                        position += 1
                    if position:
                        monobear_location = (boat_topleft[X] + 56,
                                boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
                    else:
                        monobear_location = (boat_topleft[X], boat_topleft[Y] -
                                monobear_image.get_rect().height + 16)
            # Blit the monobear
            screen.blit(monobear_image, monobear_location)
            # Add the monobear's rect into the list of monobear rects
            self.monobear_rects.append(pygame.Rect(monobear_location,
                (monobear_image.get_rect().width,
                monobear_image.get_rect().height)))
            # Draw a Monobear number
            number_font = pygame.font.SysFont("Arial", 24)
            number = number_font.render(str(x), 1, (255,0,0))
            #screen.blit(number, monobear_location)
            x += 1

    def draw_boat_text(self):
        """
        Draws the text that appears when the player attempts to move the boat
        without anybody on it.
        """
        screen = pygame.display.get_surface()
        string = "Boat cannot move without a passenger!"
        boat_rect = self.find_boat_rect()

        # Create the font
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(string, 1, (100,0,0))
        screen.blit(text, ((boat_rect.width / 2) - (text.get_rect().width / 2)
            + boat_rect.left, boat_rect.top - text.get_rect().height))

    def draw_instruction_text(self):
        """
        Draws some instructional text on top of the screen.
        """
        screen = pygame.display.get_surface()
        first_line = ("Can you move all students and monobears to the other " +
            "side without the monobears")
        second_line = " overwhelming the students?"
        first_instruction = "Click on a student or monobear to embark/disembark."
        second_instruction = "Click on the boat to move it across the river."

        # Create the font
        font = pygame.font.SysFont("Arial", 20)
        first_line_text = font.render(first_line, 1, (20,20,80))
        second_line_text = font.render(second_line, 1, (20,20,80))
        first_instruction_text = font.render(first_instruction, 1, (20,20,80))
        second_instruction_text = font.render(second_instruction, 1,
                (20,20,80))

        # Draw the fonts
        screen.blit(first_line_text, ((SCREEN_X / 2) -
            (first_line_text.get_rect().width / 2), 0))
        screen.blit(second_line_text, ((SCREEN_X / 2) -
            (second_line_text.get_rect().width / 2),
            first_line_text.get_rect().height))
        screen.blit(first_instruction_text, ((SCREEN_X / 2) -
            (first_instruction_text.get_rect().width / 2),
            (first_line_text.get_rect().height +
            second_line_text.get_rect().height)))
        screen.blit(second_instruction_text, ((SCREEN_X / 2) -
            (second_instruction_text.get_rect().width / 2) ,
            (first_line_text.get_rect().height +
            second_line_text.get_rect().height +
            first_instruction_text.get_rect().height)))

    def draw_win_lose_text(self, lose=0):
        """
        Draws the text that declares if the player has won or lost.
        """
        screen = pygame.display.get_surface()
        if lose:
            lose_font = pygame.font.SysFont("Arial", 48)
            lose_text = lose_font.render("You failed!", 1, (150,30,30))
            screen.blit(lose_text, ((SCREEN_X / 2) -
                (lose_text.get_rect().width / 2), 0))
        else:
            win_font = pygame.font.SysFont("Arial", 48)
            win_text = win_font.render("Victory!", 1, (30,150,30))
            screen.blit(win_text, ((SCREEN_X / 2) - (win_text.get_rect().width
                / 2), 0))

    def draw_water_overlay(self):
        """
        Draws a water `overlay' on the water area to make the graphics a little
        shinier.
        """
        screen = pygame.display.get_surface()

        # Create the rect
        water_rect = pygame.Rect((180, SCREEN_Y / 2), (SCREEN_X - 360, SCREEN_Y
            / 2))

        # Create a surface
        surface = pygame.Surface((SCREEN_X, SCREEN_Y))
        surface.set_colorkey((0,0,0))
        surface.set_alpha(100)
        # Fill that surface
        pygame.draw.rect(surface, (100,150,200,200), water_rect)
        # Blit the surface
        screen.blit(surface, (0,0))

    def draw_students(self):
        """
        Draws the students onto the screen, using the list of students as a
        reference.

        The list of students follow a key-value pair of student->location.
        """
        screen = pygame.display.get_surface()

        # Clean the student rects
        self.student_rects = []

        # Load the boat
        boat = self.game.find_boat()

        # Load the locations of the students
        students_locations = self.game.return_student_locations()
        # Load the boat
        boat = self.game.find_boat()
        # Load the boat location
        boat_topleft = self.find_boat_topleft()

        # We have to load the images of the students
        # Load Asahina's image
        asahina_image = pygame.image.load(os.path.join("images",
            "asahina.png"))
        # Scale Asahina's image
        asahina_image = pygame.transform.scale(asahina_image,
                ((asahina_image.get_rect().width / 3),
                asahina_image.get_rect().height / 3))
        # Load Kirigiri's image
        kirigiri_image = pygame.image.load(os.path.join("images",
            "kirigiri.png"))
        # Scale Kirigiri's image
        kirigiri_image = pygame.transform.scale(kirigiri_image,
                ((kirigiri_image.get_rect().width / 3),
                kirigiri_image.get_rect().height / 3))
        # Load Fukawa's image
        fukawa_image = pygame.image.load(os.path.join("images", "fukawa.png"))
        # Scale Fukawa's image
        fukawa_image = pygame.transform.scale(fukawa_image,
                ((fukawa_image.get_rect().width / 3),
                fukawa_image.get_rect().height / 3))

        # Now we have to find the coordinates to put the students in
        # Asahina
        if students_locations['asahina'] == 'left':
            asahina_location = (0, (SCREEN_Y / 2) -
                    asahina_image.get_rect().height + 16)
        elif students_locations['asahina'] == 'right':
            asahina_location = ((SCREEN_X - 180), (SCREEN_Y / 2) -
                    asahina_image.get_rect().height + 16)
        elif students_locations['asahina'] == 'boat':
            # We need to find Asahina's position in the boat
            position = 0
            for passenger in boat.passengers:
                if isinstance(passenger, Student):
                    if passenger.name is 'Asahina':
                        break
                position += 1
            # Now let's base Asahina's topleft position on that position found
            if position:
                asahina_location = (boat_topleft[X] + 56, boat_topleft[Y] -
                    asahina_image.get_rect().height + 12)
            else:
                asahina_location = (boat_topleft[X], boat_topleft[Y] -
                    asahina_image.get_rect().height + 12)
        # Kirigiri
        if students_locations['kirigiri'] == 'left':
            kirigiri_location = (asahina_image.get_rect().width, (SCREEN_Y / 2) -
                    kirigiri_image.get_rect().height + 16)
        elif students_locations['kirigiri'] == 'right':
            kirigiri_location = (((SCREEN_X - 180) +
                asahina_image.get_rect().width), (SCREEN_Y / 2) -
                kirigiri_image.get_rect().height + 16)
        elif students_locations['kirigiri'] == 'boat':
            # We need to find Kirigiri's position in the boat
            position = 0
            for passenger in boat.passengers:
                if isinstance(passenger, Student):
                    if passenger.name is 'Kirigiri':
                        break
                position += 1
            # Now we have to base Kirigiri's topleft position based on that
            # position
            if position:
                kirigiri_location = (boat_topleft[X] + 56, boat_topleft[Y] -
                        kirigiri_image.get_rect().height + 12)
            else:
                kirigiri_location = (boat_topleft[X], boat_topleft[Y] -
                        kirigiri_image.get_rect().height + 12)
        # Fukawa
        if students_locations['fukawa'] == 'left':
            fukawa_location = (asahina_image.get_rect().width +
                    kirigiri_image.get_rect().width, (SCREEN_Y / 2) -
                    fukawa_image.get_rect().height + 16)
        elif students_locations['fukawa'] == 'right':
            fukawa_location = (((SCREEN_X - 180) +
                asahina_image.get_rect().width +
                kirigiri_image.get_rect().width), (SCREEN_Y / 2) -
                fukawa_image.get_rect().height + 16)
        elif students_locations['fukawa'] == 'boat':
            # We need to find Fukawa's position in the boat
            position = 0
            for passenger in boat.passengers:
                if isinstance(passenger, Student):
                    if passenger.name is 'Fukawa':
                        break
                position += 1
            # Let's base Fukawa's topleft position based on that position
            if position:
                fukawa_location = (boat_topleft[X] + 56, boat_topleft[Y] -
                        fukawa_image.get_rect().height + 12)
            else:
                fukawa_location = (boat_topleft[X], boat_topleft[Y] -
                        fukawa_image.get_rect().height + 12)

        # Add the rects of the students into the list of student rects
        self.student_rects.append(pygame.Rect(asahina_location,
            (asahina_image.get_rect().width,
            asahina_image.get_rect().height)))
        self.student_rects.append(pygame.Rect(kirigiri_location,
            (kirigiri_image.get_rect().width,
            kirigiri_image.get_rect().height)))
        self.student_rects.append(pygame.Rect(fukawa_location,
            (fukawa_image.get_rect().width, fukawa_image.get_rect().height)))

        # Blit Asahina
        screen.blit(asahina_image, asahina_location)
        # Blit Kirigiri
        screen.blit(kirigiri_image, kirigiri_location)
        # Blit Fukawa
        screen.blit(fukawa_image, fukawa_location)

    def draw_button(self):
        """
        Draws the `solve' button on the bottom center that makes the AI solve
        the current problem.
        """
        screen = pygame.display.get_surface()
        
        # Load the button image
        button_image = pygame.image.load(os.path.join("images", "solve.png"))
        # Scale the image
        button_image = pygame.transform.scale(button_image,
                ((button_image.get_rect().width / 4),
                (button_image.get_rect().height / 4)))
        # Put the topleft of the boat on the center bottom
        button_topleft = ((SCREEN_X / 2) - (button_image.get_rect().width / 2),
            (SCREEN_Y - button_image.get_rect().height))
        # Create the button's rect
        self.button_rect = pygame.Rect(button_topleft,
                (button_image.get_rect().width,
                button_image.get_rect().height))
        # Blit the button image
        screen.blit(button_image, button_topleft)

    def draw_boat(self):
        """
        Draws the boat onto the screen depending on the given location.
        """
        screen = pygame.display.get_surface()
        location = self.game.find_boat().location

        # Load the boat image
        boat_image = pygame.image.load(os.path.join("images", "boat.png"))

        # Scale the image to half
        boat_image = pygame.transform.scale(boat_image,
                ((boat_image.get_rect().width / 5),
                (boat_image.get_rect().height / 5)))
        
        boat_pixel_loc = self.find_boat_topleft()

        boat_image.get_rect().topleft = boat_pixel_loc
        #self.highlight_rect(boat_image.get_rect(), (255,0,0), 1)

        # Blit the boat to that location
        screen.blit(boat_image, boat_pixel_loc)

    def find_boat_topleft(self):
        """
        Finds the the coordinates where we should draw the boat. Could be
        useful for drawing the boat's passengers as well.
        """
        boat = self.game.find_boat().location

        # Load the boat image
        boat_image = pygame.image.load(os.path.join("images", "boat.png"))

        # Scale the image to half
        boat_image = pygame.transform.scale(boat_image,
                ((boat_image.get_rect().width / 5),
                (boat_image.get_rect().height / 5)))

        # Get the coordinates where we should put the boat in
        if boat is 'right':
            boat_pixel_loc = ((SCREEN_X - 180) -
                    boat_image.get_rect().width, (SCREEN_Y / 2) - 8)
        else:
            boat_pixel_loc = (180, (SCREEN_Y / 2) - 8)

        return boat_pixel_loc

    def find_boat_rect(self):
        """
        Finds the rect corresponding to the boat, then returns it.
        """
        boat = self.game.find_boat().location

        # Load the boat image
        boat_image = pygame.image.load(os.path.join("images", "boat.png"))

        # Scale the image to half
        boat_image = pygame.transform.scale(boat_image,
                ((boat_image.get_rect().width / 5),
                (boat_image.get_rect().height / 5)))

        if boat is 'right':
            boat_pixel_loc = ((SCREEN_X - 180) -
                    boat_image.get_rect().width, (SCREEN_Y / 2) -
                    (boat_image.get_rect().height / 2))
        else:
            boat_pixel_loc = (180, (SCREEN_Y / 2) -
                    (boat_image.get_rect().height / 2))

        rect = boat_image.get_rect()
        rect.topleft = boat_pixel_loc

        return rect
    
    def __init__(self, game):
        self.game = game
        self.student_rects = []
        self.monobear_rects = []
        self.button_rect = None
