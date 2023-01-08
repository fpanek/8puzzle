class PuzzleNode:
    """
    The 8 puzzle node consists of:
        * The puzzle as 2D array of values
        * g = total cost from the start node
        * h = estimated cost to the goal
        * f = sum of all path costs (g + h); lowest f value will be the next node to be analyzed
    """

    def __init__(self, puzzle, g, h):
        self.g = g
        self.h = h
        self.puzzle = puzzle
