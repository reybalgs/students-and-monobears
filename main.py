#!/usr/bin/python

# main.py
#
# Main file for the game.

# Important imports
import random, os, sys, pygame, pdb
from pygame.locals import *

from game import *
from renderer import *
from ai_solver import *

##############################################################################
# CONSTANTS
##############################################################################

# Screen resolution
SCREEN_X = 640
SCREEN_Y = 480

# Game frame rate
FPS = 15

# Delay when the AI makes a move
MOVE_DELAY = 250

# Initialize the sound mixer
pygame.mixer.init()

# Load the sounds that will be used
click_sound = pygame.mixer.Sound(os.path.join("sounds", "click.ogg"))
win_sound = pygame.mixer.Sound(os.path.join("sounds", "win.ogg"))
lose_sound = pygame.mixer.Sound(os.path.join("sounds", "lose.ogg"))

def main():
    # Load a clock to limit the game FPS
    clock = pygame.time.Clock()

    pygame.init()

    # Initialize the game main screen
    window = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption('Students and Monobears')
    screen = pygame.display.get_surface()

    # Initialize a game
    game = Game()

    # Initialize the AI
    ai = AI(game)

    # Flag that tracks if the AI has to solve the problem
    ai_solving = False

    # DEBUG: Set entity locations
    #game.find_boat().location = 'left'
    #game.find_student('Asahina').location = 'left'
    #game.find_student('Kirigiri').location = 'left'
    #game.find_student('Fukawa').location = 'left'
    #game.find_monobear(0).location = 'left'
    #game.find_monobear(1).location = 'left'
    #game.find_monobear(2).location = 'left'
    #game.board_boat(game.find_student('Kirigiri'))
    #game.board_boat(game.find_student('Asahina'))
    #game.board_boat(game.find_student('Fukawa'))
    #game.board_boat(game.find_monobear(0))
    #game.board_boat(game.find_monobear(1))
    #game.board_boat(game.find_monobear(2))
    #game.move_boat()

    # Initialize a renderer for the graphics
    renderer = Renderer(game)

    # Play the music of the game
    pygame.mixer.music.load(os.path.join("sounds", "music.ogg"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


    # Main game loop
    while True:
        # Tick the game clock
        clock.tick(FPS)

        ######################################################################
        # GAME LOGIC
        ######################################################################

        # Something should go here
        if(game.check_if_lost()):
            lose_sound.play()
            pygame.mixer.music.stop()
            print('You lose!')
            pygame.time.wait(int(lose_sound.get_length() * 1000))
            return 0
        if(game.check_if_won()):
            win_sound.play()
            pygame.mixer.music.stop()
            print('You win!')
            pygame.time.wait(int(win_sound.get_length() * 1000))
            break

        # If the AI is supposed to solve the game, make it so
        if ai_solving:
            # Find a route for the current game state
            ai.solve()
            # Make a move depending on the AI path
            ai.make_move(ai.path.pop(1))
            click_sound.play()
            # Put some kind of delay
            pygame.time.wait(MOVE_DELAY)
        
        ######################################################################
        # EVENT HANDLING
        ######################################################################

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if not ai_solving:
                if event.type == MOUSEBUTTONDOWN:
                    eventX = event.pos[0]
                    eventY = event.pos[1]
                    click_sound.play()
                    boat_rect = renderer.find_boat_rect()
                    # Check if the user clicked on the boat
                    if((eventX > boat_rect.left and eventX < boat_rect.right)
                            and (eventY > boat_rect.top and eventY <
                            boat_rect.bottom)):
                        # Player has pressed the boat
                        game.move_boat()
                    elif((eventX > renderer.button_rect.left and eventX <
                            renderer.button_rect.right) and (eventY >
                            renderer.button_rect.top and eventY <
                            renderer.button_rect.bottom)):
                        # Player has pressed the solve button
                        print('AI now solving the game!')
                        ai_solving = True
                    else:
                        for rect in renderer.student_rects:
                            # Check if the user pressed one of the student rects
                            if((eventX > rect.left and eventX < rect.right) and
                                    (eventY > rect.top and eventY <
                                    rect.bottom)):
                                if(renderer.student_rects.index(rect) is 0):
                                    # Player has selected Asahina
                                    student = game.find_student('Asahina')
                                elif(renderer.student_rects.index(rect) is 1):
                                    # Player has selected Kirigiri
                                    student = game.find_student('Kirigiri')
                                elif(renderer.student_rects.index(rect) is 2):
                                    # Player has selected Fukawa
                                    student = game.find_student('Fukawa')
                                # Check if we have to make the student board or
                                # disembark the boat
                                if(game.check_if_in_boat(student)):
                                    game.disembark_boat(student)
                                else:
                                    game.board_boat(student)
                        for rect in renderer.monobear_rects:
                            # Check if the user pressed one of the monobear rects
                            if((eventX > rect.left and eventX < rect.right) and
                                    (eventY > rect.top and eventY <
                                    rect.bottom)):
                                if(renderer.monobear_rects.index(rect) is 0):
                                    # Player has selected Monobear 0
                                    monobear = game.find_monobear(0)
                                elif(renderer.monobear_rects.index(rect) is 1):
                                    # Player has selected Monobear 1
                                    monobear = game.find_monobear(1)
                                elif(renderer.monobear_rects.index(rect) is 2):
                                    # Player has selected Monobear 2
                                    monobear = game.find_monobear(2)
                                # Check if we have to make the monobear board
                                # or disembark the boat
                                if(game.check_if_in_boat(monobear)):
                                    game.disembark_boat(monobear)
                                else:
                                    game.board_boat(monobear)

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

        # Draw the water
        renderer.draw_water_overlay()

        # Draw the solve button
        renderer.draw_button()

        # Update everything
        pygame.display.flip()

if __name__ == '__main__':
    main()
