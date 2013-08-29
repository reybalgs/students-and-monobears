# entity.py
#
# Superclass for all entities in the game.

class Entity(object):
    def change_location(self):
        """
        Switches the location of this entity.
        """
        if self.location is 'right':
            self.location = 'left'
        else:
            self.location = 'right'

    def __init__(self, location='right'):
        """
        Initialization function for all entities.

        location
            The location you want the entity to initialize on. Could be the
            left or the right side of the game.
        """
        self.location = location
