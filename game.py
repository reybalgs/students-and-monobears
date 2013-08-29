# game.py
#
# Contains the game logic for the game.

from entity import Entity
from student import Student
from boat import Boat

class Game():
    def __init__(self):
        """
        Initialization function for a game of Students and Monobears.
        """
        # Create a list of entities on the left side
        self.left_side_entities = []
        # Create a list of entities on the right side
        self.right_side_entities = []

        # Put the boat on the right side of the game
        boat = Boat('right')
        self.right_side_entities.append(boat)

        # Create three students on the right side
        for x in range(0, 3):
            if(x is 0):
                name = 'Fukawa'
            elif(x is 1):
                name = 'Kirigiri'
            elif(x is 2):
                name = 'Asahina'
            print('Student name is ' + name)
            student = Student(name)
            self.right_side_entities.append(student)

        # Create three monobears on the right side
        for x in range(0, 3):
            monobear = Monobear()
            self.right_side_entities.append(monobear)
