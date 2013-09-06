# ai_solver.py
#
# Python file containing the source code for the game's AI.

import random, pdb

from student import *
from monobear import *

class Node():
    def print_node(self):
        """
        Prints the node.
        """
        print('<' + str(self.cannibals) + ',' + str(self.missionaries) + ',' +
                str(self.boat) + '>')
        if self.parent is not None:
            print('From <' + str(self.parent.cannibals) + ',' +
                    str(self.parent.missionaries) + ',' + str(self.parent.boat)
                    + '>')

    def is_valid(self):
        """
        Checks whether or not the node is valid.
        """
        if((self.missionaries <= 3 and self.missionaries >= 0) and
                (self.cannibals <= 3 and self.cannibals >= 0)):
            if(self.missionaries == 0):
                return True
            elif(self.missionaries == 3):
                if(self.cannibals <= self.missionaries):
                    return True
            else:
                if((self.cannibals <= self.missionaries) and abs(self.cannibals -
                        3) <= abs(self.missionaries - 3)):
                    return True
                else:
                    return False
        else:
            return False

    def equal_to(self, node):
        """
        Returns a boolean value depending on whether or not this node is equal
        to the node given as an argument.
        """
        if(self.cannibals == node.cannibals and self.missionaries ==
                node.missionaries and self.boat == node.boat):
            return True
        else:
            return False

    def __init__(self, cannibals, missionaries, boat, parent=None,
            viable=True):
        self.parent = parent
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.viable = viable
        self.successors = []

class AI():
    def is_node_inside_list(self, node, list):
        """
        Checks whether the given node is inside the given list, and returns the
        appropriate boolean value.
        """
        for x in list:
            if(node.missionaries == x.missionaries and node.cannibals ==
                    x.cannibals and node.boat == x.boat):
                return True
        return False

    def check_nodes_viable(self):
        """
        Returns a boolean value on whether or not some nodes in the list are
        still viable.
        """
        for node in self.nodes:
            if node.viable:
                return True
        return False

    def find_successor_nodes(self, node):
        """
        Returns viable successor nodes of the given node.
        """
        #pdb.set_trace()
        successors = []
        print('Evaluating successors of node:')
        node.print_node()
        if node.boat == 1:
            # Boat is on the right side
            print('Node is on right side!')
            # First option: Send two cannibals into left side
            successor = Node(node.cannibals - 2, node.missionaries, 0, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Second option: Send two missionaries into left side
            successor = Node(node.cannibals, node.missionaries - 2, 0, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not self.is_node_inside_list(successor,
                    self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Third option: Send one cannibal and one missionary into left side
            successor = Node(node.cannibals - 1, node.missionaries - 1, 0,
                    node) 
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not self.is_node_inside_list(successor,
                    self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Fourth option: Send one cannibal into left side
            successor = Node(node.cannibals - 1, node.missionaries, 0, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not self.is_node_inside_list(successor,
                    self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Fifth option: Send one missionary into left side
            successor = Node(node.cannibals, node.missionaries - 1, 0, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
        elif node.boat == 0:
            # Boat is on the left side
            print('Boat is on left side!')
            # First option: Send two cannibals into right side
            successor = Node(node.cannibals + 2, node.missionaries, 1, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Second option: Send two missionaries into right side
            successor = Node(node.cannibals, node.missionaries + 2, 1, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not self.is_node_inside_list(successor,
                    self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Third option: Send one cannibal and one missionary into right
            # side
            successor = Node(node.cannibals + 1, node.missionaries + 1, 1, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Fourth option: Send one cannibal into right side
            successor = Node(node.cannibals + 1, node.missionaries, 1, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
            # Fifth option: Send one missionary into right side
            successor = Node(node.cannibals, node.missionaries + 1, 1, node)
            print('Evaluating node:')
            successor.print_node()
            if(successor.is_valid() and not
                    self.is_node_inside_list(successor, self.closed_nodes)):
                successor.print_node()
                print(' is valid!')
                successors.append(successor)
        # Print the successors
        print('Successors:')
        for x in successors:
            x.print_node()
        return successors

    def recreate_path(self, node):
        if node.parent:
            # Node has a parent, set do-while flag
            parent = True
        else:
            # Current node has no parents, there is no path
            return
        current_node = node
        while parent:
            # Add the current node into the path
            self.path.append(current_node)
            if current_node.parent:
                # Current node has a parent
                current_node = current_node.parent
            else:
                # The current node has no parent
                parent = False
                # Reverse the path
                self.path.reverse()
                return self.path

    def make_move(self, next_node):
        """
        Function that facilitates the movement of the AI. Moves the game
        environment depending on the given node. 
        """
        # Get the current node the AI is on
        current_node = self.find_current_node()

        # DEBUG: Print those nodes
        print('Current node: ')
        current_node.print_node()
        print('Next node: ')
        next_node.print_node()

        # Get the boat from the game
        boat = self.game.find_boat()
        # Disembark all people from the boat
        for passenger in boat.passengers:
            self.game.disembark_boat(passenger)

        # Move the game according to the difference between the current node
        # and the next node
        if boat.location is 'left':
            if(next_node.missionaries > current_node.missionaries):
                # Board all missing missionaries onto the boat
                for x in range(current_node.missionaries,
                        next_node.missionaries):
                    # Get a random student from the left side
                    student = random.choice([entity for entity in
                        self.game.get_potential_passengers_on_side('left') if
                        isinstance(entity, Student)])
                    # Make that student board the boat
                    self.game.board_boat(student)
            if(next_node.cannibals > current_node.cannibals):
                # Board all missing cannibals onto the boat
                for x in range(current_node.cannibals, next_node.cannibals):
                    # Get a random monobear from the left side
                    monobear = random.choice([entity for entity in
                        self.game.get_potential_passengers_on_side('left') if
                        isinstance(entity, Monobear)])
                    # Make that monobear board the boat
                    self.game.board_boat(monobear)
            # Move the boat
            self.game.move_boat()
            # Disembark all passengers from the boat
            for passenger in boat.passengers:
                self.game.disembark_boat(passenger)
        elif boat.location is 'right':
            if(next_node.missionaries < current_node.missionaries):
                # Board all missing missionries onto the boat
                for x in range(next_node.missionaries,
                        current_node.missionaries):
                    # Get a random student from the right side
                    student = random.choice([entity for entity in
                        self.game.get_potential_passengers_on_side('right') if
                        isinstance(entity, Student)])
                    # Make that student board the boat
                    self.game.board_boat(student)
            if(next_node.cannibals < current_node.cannibals):
                # Board all missing cannibals onto the boat
                for x in range(next_node.cannibals, current_node.cannibals):
                    # Get a random monobear form the right side
                    monobear = random.choice([entity for entity in
                        self.game.get_potential_passengers_on_side('right') if
                        isinstance(entity, Monobear)])
                    # Make that monobear board the boat
                    self.game.board_boat(monobear)
            # Move the boat
            self.game.move_boat()
            # Disembark all passengers from the boat
            self.game.disembark_boat_pop()
            self.game.disembark_boat_pop()

    def is_desired_node(self, node):
        """
        Returns a boolean value on whether or not the node passed as an
        argument is the desired final node.
        """
        if(node.cannibals == 0 and node.missionaries == 0 and node.boat == 0):
            return True
        else:
            return False

    def find_current_node(self):
        """
        Finds the node that the game is currently on.
        """
        # Get the number of missionaries and cannibals on the right side
        missionaries = self.game.count_entities_in_side('student', 'right')
        cannibals = self.game.count_entities_in_side('monobear', 'right')

        # Get the location of the boat
        if(self.game.find_boat().location is 'right'):
            boat = 1
        else:
            boat = 0

        # Create the node
        current_node = Node(cannibals, missionaries, boat)
        current_node.print_node()

        # Return that node
        return current_node

    def solve(self):
        """
        Solves the problem.
        """
        self.open_nodes = []
        self.closed_nodes = []
        self.path = []
        # First we need to find the possible node states of the game.
        # Get the initial node
        self.open_nodes.append(self.find_current_node())
        while(len(self.open_nodes)):
            current_node = self.open_nodes.pop(0)
            print('Current node is: ')
            current_node.print_node()
            # Check if the current node is the desired node
            if self.is_desired_node(current_node):
                print('Final node is found!')
                self.recreate_path(current_node)
                return
            
            # Put it in the list of closed nodes
            self.closed_nodes.append(current_node)

            # Find the states that the node can move to
            # First we have to clean up the successors of the current node
            current_node.successors = []
            current_node.successors = self.find_successor_nodes(current_node)
            # Add those successors to the AI's list of nodes
            self.open_nodes += [successor for successor in
                    current_node.successors if not
                    self.is_node_inside_list(successor, self.open_nodes)]
            print('Open nodes:')
            for node in self.open_nodes:
                # Print all open nodes
                node.print_node()
            print('Closed nodes:')
            for node in self.closed_nodes:
                # Print all closed nodes
                node.print_node()
            #pdb.set_trace()

    def __init__(self, game):
        """
        Initialization function for the AI. Requires a S&M game to work
        """
        self.game = game
        self.open_nodes = []
        self.closed_nodes = []
        # Path the AI has to follow
        self.path = []
        print('AI initialized.')
