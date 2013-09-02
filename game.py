# game.py
#
# Contains the game logic for the game.

import pdb

from entity import Entity
from student import Student
from boat import Boat
from monobear import Monobear

class Game():
    def check_if_won(self):
        """
        Evaluates the current game environment and returns whether or not the
        player has won (all students and monobears on the left side) or not.
        """
        if(self.count_entities_in_side('student', 'left') == 3 and
                self.count_entities_in_side('monobear', 'left') == 3 and
                len(self.find_boat().passengers) == 0):
            return True
        else:
            return False

    def print_entity_information(self, entity):
        """
        Prints information specific to the entity passed as an argument.
        """
        if isinstance(entity, Student):
            print('Student: ' + entity.name)
        elif isinstance(entity, Monobear):
            print('Monobear no. ' + str(entity.number))
    
    def get_potential_passengers_on_side(self, side):
        """
        Puts all potential passenger entities on the given side, and returns
        them in a list.
        """
        list = []
        if side is 'left':
            for entity in self.left_side_entities:
                if isinstance(entity, Student):
                    list.append(entity)
                elif isinstance(entity, Monobear):
                    list.append(entity)
        else:
            for entity in self.right_side_entities:
                if isinstance(entity, Student):
                    list.append(entity)
                elif isinstance(entity, Monobear):
                    list.append(entity)
        return list

    def display_statistics(self):
        """
        Displays every bit of information on the game.
        """
        print('\nCurrent Status')
        print('LEFT SIDE')
        if len(self.left_side_entities) == 0:
            print('EMPTY!')
        else:
            for entity in self.left_side_entities:
                if isinstance(entity, Student):
                    print('Student ' + entity.name)
                elif isinstance(entity, Monobear):
                    print('Monobear ' + str(entity.number))
                elif isinstance(entity, Boat):
                    print('Boat: [')
                    for passenger in entity.passengers:
                        if isinstance(passenger, Student):
                            print('Student ' + passenger.name)
                        elif isinstance(passenger, Monobear):
                            print('Monobear ' + str(passenger.number))
                    print(']')
        print('\nRIGHT SIDE')
        if len(self.right_side_entities) == 0:
            print('EMPTY!')
        else:
            for entity in self.right_side_entities:
                if isinstance(entity, Student):
                    print('Student ' + entity.name)
                elif isinstance(entity, Monobear):
                    print('Monobear ' + str(entity.number))
                elif isinstance(entity, Boat):
                    print('Boat: [')
                    for passenger in entity.passengers:
                        if isinstance(passenger, Student):
                            print('Student ' + passenger.name)
                        elif isinstance(passenger, Monobear):
                            print('Monobear ' + str(passenger.number))
                    print(']')
    
    def check_if_lost(self):
        """
        Evaluates the current game environment and returns whether or not the
        player has lost (monobears > students on one side) or not.
        """
        # Start with the left side
        left_students_count = self.count_entities_in_side('student', 'left')
        left_monobears_count = self.count_entities_in_side('monobear', 'left')

        if(left_monobears_count > left_students_count and left_students_count >
                0):
            return True
        
        # Then go to the right side
        right_students_count = self.count_entities_in_side('student', 'right')
        right_monobears_count = self.count_entities_in_side('monobear',
                'right')

        if(right_monobears_count > right_students_count and
                right_students_count > 0):
            return True

        # There is no losing condition yet
        return False

    def list_entities(self, entity):
        """
        Gets all the entities of the type entity from both sides of the game
        and returns them in a list.
        """
        entity_list = []

        if entity is 'student' or entity is 'students':
            print('Listing students...')
            for x in self.left_side_entities:
                if isinstance(x, Student):
                    entity_list.append(x)
            for x in self.right_side_entities:
                if isinstance(x, Student):
                    entity_list.append(x)
            for x in self.find_boat().passengers:
                if isinstance(x, Student):
                    entity_list.append(x)
        elif entity is 'monobear' or entity is 'monobears':
            print('Listing monobears...')
            for x in self.left_side_entities:
                if isinstance(x, Monobear):
                    entity_list.append(x)
            for x in self.right_side_entities:
                if isinstance(x, Monobear):
                    entity_list.append(x)
            for x in self.find_boat().passengers:
                if isinstance(x, Monobear):
                    entity_list.append(x)
        return entity_list

    def find_monobear(self, number):
        """
        Finds the monobear with the given number and returns it.
        """
        # First, get a list of all monokumas
        monobears = self.list_entities('monobear')
        # Find the monobear within that list
        for monobear in monobears:
            if monobear.number is number:
                print('Monobear No. ' + str(monobear.number) + ' is found!')
                return monobear
        print('Monobear no. ' + str(number) + ' not found!')

    def find_student(self, name):
        """
        Finds the student with the given name and returns it.
        """
        # First, get the list of all the students
        students = self.list_entities('student')
        print(str(students))

        # Find the student within that list
        for student in students:
            if student.name is name:
                print('Student ' + student.name + ' is found!')
                return student
        print('Student ' + name + ' not found!')

    def count_entities_in_side(self, entity, side):
        """
        Counts the number of given entities in the given side, then returns the
        count as a number value.
        """
        count = 0
        if(entity is 'student' or entity is 'students'):
            if(side is 'right'):
                for entity in self.right_side_entities:
                    if(isinstance(entity, Student)):
                        count += 1
                    elif(isinstance(entity, Boat)):
                        for passenger in entity.passengers:
                            if(isinstance(passenger, Student)):
                                count += 1
            else:
                for entity in self.left_side_entities:
                    if(isinstance(entity, Student)):
                        count += 1
                    elif(isinstance(entity, Boat)):
                        for passenger in entity.passengers:
                            if(isinstance(passenger, Student)):
                                count += 1
        else:
            if(side is 'right'):
                for entity in self.right_side_entities:
                    if(isinstance(entity, Monobear)):
                        count += 1
                    elif(isinstance(entity, Boat)):
                        for passenger in entity.passengers:
                            if(isinstance(passenger, Monobear)):
                                count += 1
            else:
                for entity in self.left_side_entities:
                    if(isinstance(entity, Monobear)):
                        count += 1
                    elif(isinstance(entity, Boat)):
                        for passenger in entity.passengers:
                            if(isinstance(passenger, Monobear)):
                                count += 1
        return count

    def get_status_tuple(self):
        """
        Returns the current state of the game in the format (monobears,
        students, boat) in the right side
        """
        boat_right = 0
        if self.find_boat().location == 'right':
            boat_right = 1
        return (self.count_entities_in_side('monobear', 'right'),
                self.count_entities_in_side('student', 'right'),
                boat_right)

    def move_boat(self):
        """
        Moves the boat from its current side to the other.

        Note that the boat cannot move without anybody on it.
        """
        # First, find the boat
        boat = self.find_boat()

        if len(boat.passengers):
            # There's a passenger in the boat
            # Pop the boat from the current side it is on and append it to the
            # other.
            if boat.location is 'left':
                # Get the index of the boat
                index = self.left_side_entities.index(boat)
                self.right_side_entities.append(self.left_side_entities.pop(index))
                # Change the location of the boat and its passengers
                boat.location = 'right'
                for passenger in boat.passengers:
                    passenger.location = 'right'
            else:
                index = self.right_side_entities.index(boat)
                self.left_side_entities.append(self.right_side_entities.pop(index))
                boat.location = 'left'
                for passenger in boat.passengers:
                    passenger.location = 'left'
            print('Boat moved to the ' + boat.location)
        else:
            # There are no passengers, boat is not moving
            print('Boat has no passengers, boat cannot move by itself!')

    def disembark_boat_pop(self):
        """
        Disembarks the last entity on the boat by popping it from the boat's
        list of passengers.
        """
        # Find the boat
        boat = self.find_boat()

        # Check if the boat actually has passengers
        if(len(boat.passengers) <= 0):
            print('Boat has no passengers!')
            return
        else:
            if boat.location is 'left':
                self.left_side_entities.append(boat.passengers.pop())
            else:
                self.right_side_entities.append(boat.passengers.pop())

    def disembark_boat(self, entity):
        """
        Disembarks the given entity from the boat, and puts it in the side the
        boat is currently on, if that entity is inside the boat.
        """
        # First, find the boat
        boat = self.find_boat()

        # Now see if the given entity is in the boat
        if entity in boat.passengers:
            # Get the index of the entity within the boat's passenger list
            index = boat.passengers.index(entity)
            # Pop the entity from the boat and put them on the boat's current
            # side
            if boat.location is 'left':
                self.left_side_entities.append(boat.passengers.pop(index))
            else:
                self.right_side_entities.append(boat.passengers.pop(index))
        else:
            print('Entity ' + str(entity) + ' is not in boat!')

    def find_boat(self, side=None):
        """
        Finds the boat on the given side and returns it. If no side is given,
        this function will find the boat on both sides.
        """
        if side is None:
            for entity in self.right_side_entities:
                if isinstance(entity, Boat):
                    boat = entity
            for entity in self.left_side_entities:
                if isinstance(entity, Boat):
                    boat = entity
        elif side is 'left':
            for entity in self.left_side_entities:
                if isinstance(entity, Boat):
                    boat = entity
        elif side is 'right':
            for entity in self.right_side_entities:
                if isinstance(entity, Boat):
                    boat = entity
        return boat

    def board_boat(self, entity):
        """
        Boards the given entity onto the boat, if the boat is preset on the
        side the entity is on.
        """
        # Find the boat
        boat = self.find_boat()
        # DEBUG: Print entity information
        #print('Passed entity:')
        #self.print_entity_information(entity)
        # Check if the boat already contains the given entity
        if entity in boat.passengers:
            print(str(entity) + ' already in boat!')
            return
        else:
            # Check if the given entity is on the same side as the boat
            print('Entity location: ' + entity.location + ' Boat location : ' +
                    boat.location)
            if entity.location is boat.location:
                # Check if the boat is full
                if len(boat.passengers) == 2:
                    print('Boat is full!')
                    return
                else:
                    # Get the index of the entity from the list
                    if(entity.location is 'right'):
                        index = self.right_side_entities.index(entity)
                        # Pop the entity from the x-side entities list and put
                        # it on the boat
                        boat.passengers.append(self.right_side_entities.pop(
                            index))
                    else:
                        index = self.left_side_entities.index(entity)
                        # Pop the entity from the x-side entities list and put
                        # it on the boat
                        boat.passengers.append(self.left_side_entities.pop(
                            index))
            else:
                # The entity is not on the same side as the boat, it cannot
                # board the boat
                print('Given entity not on the same side as the boat!')
                return

    def __init__(self):
        """
        Initialization function for a game of Students and Monobears.
        """
        # Create a list of entities on the left side
        self.left_side_entities = []
        # Create a list of entities on the right side
        self.right_side_entities = []

        # Put the boat on the right side of the game
        boat = Boat()
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
            print(student.name + ' is on the ' + student.location + ' side')
            self.right_side_entities.append(student)

        # Create three monobears on the right side
        for x in range(0, 3):
            monobear = Monobear(x)
            print('Monobear ' + str(monobear.number) + ' created!')
            print('Monobear ' + str(monobear.number) + ' is on the ' +
                    monobear.location + ' side')
            self.right_side_entities.append(monobear)
