# boat.py
#
# Contains the code for the boat in the game.

from entity import Entity
from student import Student
from monobear import Monobear

class Boat(Entity):
    def check_full(self):
        """
        Returns a boolean value on whether or not the boat is full or not.
        """
        if(len(self.passengers) >= 2):
            return True
        else:
            return False

    def list_passengers(self):
        """
        Lists all passengers currently inside the boat
        """
        if(len(self.passengers) <= 0):
            print('No passengers inside the boat!')
            return
        else:
            print('Passengers inside boat: ')
            for passenger in self.passengers:
                # Check the type of passenger inside the boat
                if(isinstance(passenger, Student)):
                    # Current passenger is a student
                    print('Student: ' + passenger.name)
                elif(isinstance(passenger, Monobear)):
                    # Current passenger is a monobear
                    print('Monobear ' + str(passenger.number))

    def __init__(self, firstPassenger = None, secondPassenger = None):
        super(Boat, self).__init__()
        self.passengers = []
        if firstPassenger is not None:
            self.passengers.append(firstPassenger)
        if secondPassenger is not None:
            self.passengers.append(secondPassenger)
