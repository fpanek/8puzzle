from eight_puzzle.create_puzzle import  *
from eight_puzzle.puzzle_functions import *
from eight_puzzle.puzzle_node import *
from eight_puzzle.priority_queue import *

#definition of puzzle - 2d array
#     0 1 2 (col Axis - second value of array)
#  0 |0|1|2|
#  1 |3|4|5|
#  2 |6|7|8|
#  (row Axis first value of the array)
if __name__ == '__main__':

    puzzleArray = []
    puzzleArray.append([ [0,8,2], [3,7,5], [6,4,1]])  #hammming distance = 4, manhattan distance = 8
    puzzleArray.append([ [3,8,0], [5,4,1], [7,6,2]])
    puzzleArray.append([ [0,2,3], [1,7,8], [5,6,4]])

    #the defined goal state
    puzzle_goal = [ [0,1,2], [3,4,5], [6,7,8]] #hammming distance = 4, manhattan distance = 8

    for x in puzzleArray:
        print("solving puzzle: ", x)
        print("unsorted field:")
        print_puzzle(x)
        resolved_puzzle = solve_puzzle(x, puzzle_goal, "h")
        print("sorted field:")
        print_puzzle(resolved_puzzle)





