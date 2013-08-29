# student.py
#
# Class for the student in the game. The students are considered the game's
# "missionaries".

from entity import Entity

class Student(Entity):
    def __init__(self, location='right'):
        super.__init__(self, location='right')
