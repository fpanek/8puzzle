from eight_puzzle.create_puzzle import  *
from eight_puzzle.puzzle_functions import *

#definition of puzzle - 2d array
#     0 1 2 (col Axis - first value of array)
#  0 |0|1|2|
#  1 |3|4|5|
#  2 |6|7|8|
#  (row Axis second value of the array)
if __name__ == '__main__':
    #puzzle = create_random_puzzle()
    #Test pattern:
    puzzle = [ [0,8,2], [3,7,5], [6,4,1]] #hammming distance = 4, manhattan distance = 8
    print_puzzle(puzzle)
    hamming_distance = calculate_hamming_distance(puzzle)
    print("hamming distance of the given puzzle is: ", hamming_distance)
    manhattan_distance = calculate_manhattan_distance(puzzle)
    print("manhattan distance of the given puzzle is: ", manhattan_distance)