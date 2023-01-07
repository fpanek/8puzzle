"""
8 puzzle node
node consists of:
    *)the puzzle as 2d array
    *)g - the total cost from the start node
    *)h - the estimated cost to the goal
    *)f - sum of all path costs -> g + h (lowest f value will be the next node to be analyzed)
    *)parentnode - die parent node der aktuellen node
"""

class puzzle_node():

##__init__ is maybe comparable to the constructor in java
    def __init__(self,puzzle, g, h):
        #Todo implement creation of object and values
        self.g = g
        self.h = h
        self.puzzle = puzzle


