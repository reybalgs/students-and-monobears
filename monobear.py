# monobear.py
#
# Contains the code for the Monobears in the game.

from entity import Entity

class Monobear(Entity):
    def __init__(self, number):
        super(Monobear, self).__init__()
        self.number = number
