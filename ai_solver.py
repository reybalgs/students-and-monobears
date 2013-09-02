# ai_solver.py
#
# Python file containing the source code for the game's AI.

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

    def __init__(self, parent=None, cannibals, missionaries, boat,
            viable=True):
        self.parent = parent
        self.cannibals = cannibals
        self.missionaries = missionaries
        self.boat = boat
        self.viable = viable
        self.successors = []

class AI():
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
        successors = []
        if node.boat:
            print('Evaluating node:')
            node.print_node()
            # Boat is on the right side
            # First option: Send two cannibals into left side
            if((node.cannibals - 2) >= 0 and (node.cannibals - 2) <
                    node.missionaries):
                successors.append(Node(node, node.cannibals - 2,
                    node.missionaries, 0))
            # Second option: Send two missionaries into left side
            if((node.missionaries - 2) >= 0 and (node.missionaries - 2) >
                    node.cannibals):
                successors.append(Node(node, node.cannibals, node.missionaries
                    - 2, 0))
            # Third option: Send one cannibal and one missionary into left side
            if((node.missionaries - 1) >= 0 and (node.cannibals - 1) >= 0 and
                    (node.missionaries - 1) > (node.cannibals - 1)):
                successors.append(Node(node, node.cannibals - 1,
                    node.missionaries - 1, 0))
            # Fourth option: Send one cannibal into left side
            if((node.cannibals - 1) >= 0 and (node.cannibals - 1) <
                    node.missionaries):
                successors.append(Node(node, node.cannibals - 1,
                    node.missionaries, 0))
            # Fifth option: Send one missionary into left side
            if((node.missionaries - 1) >= 0 and (node.missionaries - 1) >
                    node.cannibals):
                successors.append(Node(node, node.cannibals, node.missionaries
                    - 1, 0))
        else:
            # Boat is on the left side
            # First option: Send two cannibals into right side
            if((node.cannibals + 2) <= 3 and (node.cannibals + 2) <
                    node.missionaries):
                successors.append(Node(node, node.cannibals + 2,
                    node.missionaries, 1))
            # Second option: Send two missionaries into right side
            if((node.missionaries + 2) <= 3 and (node.missionaries + 2) >
                    node.cannibals):
                successors.append(Node(node, node.cannibals, node.missionaries
                    + 2, 1))
            # Third option: Send one cannibal and one missionary into right
            # side
            if((node.missionaries + 1) <= 3 and (node.cannibals + 1) <= 3 and
                    (node.cannibals + 1) < (node.missionaries + 1)):
                successors.append(Node(node, node.cannibals + 1,
                    node.missionaries + 1, 1))
            # Fourth option: Send one cannibal into right side
            if((node.cannibals + 1) <= 3 and (node.cannibals + 1) <
                    node.missionaries):
                successors.append(Node(node, node.cannibals + 1,
                    node.missionaries, 1))
            # Fifth option: Send one missionary into right side
            if((node.missionaries + 1) <= 3 and (node.missionaries + 1) >
                    node.cannibals, 1):
                successors.append(Node(node, node.cannibals, node.missionaries
                    + 1, 1))
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
            return self.path.append(node)
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

    def is_desired_node(self, node):
        """
        Returns a boolean value on whether or not the node passed as an
        argument is the desired final node.
        """
        if(node.cannibals == 0 and node.missionaries == 0 and node.boat == 0):
            return True
        else:
            return False

    def solve(self, game):
        """
        Solves the problem.
        """
        self.open_nodes = []
        self.closed_nodes = []
        self.path = []
        # First we need to find the possible node states of the game.
        # Get the initial node
        self.open_nodes.append(Node(None, 3, 3, 1))
        while(len(self.open_nodes)):
            current_node = self.open_nodes.pop(0)
            # Check if the current node is the desired node
            if is_desired_node(current_node):
                self.recreate_path(current_node)
            
            # Remove the node from the list of open nodes
            self.open_nodes.pop(self.open_nodes.index(current_node))
            # Put it in the list of closed nodes
            self.closed_nodes.append(current_node)

            # Find the states that the node can move to
            current_node.successors = self.find_successor_nodes(current_node)
            # Add those successors to the AI's list of nodes
            self.open_nodes += current_node.successors

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
