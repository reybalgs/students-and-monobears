# boat.py
#
# Contains the code for the boat in the game.

from entity import Entity

class Boat(Entity):
    def __init__(self, firstPassenger = None, secondPassenger = None):
        super.__init__(self)
        self.firstPassenger = firstPassenger
        self.secondPassenger = secondPassenger
