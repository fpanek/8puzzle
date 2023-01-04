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
    #puzzle = create_random_puzzle()
    #Test pattern:
    puzzle = [ [0,8,2], [3,7,5], [6,4,1]] #hammming distance = 4, manhattan distance = 8

    #print_puzzle(puzzle)
    #hamming_distance = calculate_hamming_distance(puzzle)
    #print("hamming distance of the given puzzle is: ", hamming_distance)
    #manhattan_distance = calculate_manhattan_distance(puzzle)
    #print("manhattan distance of the given puzzle is: ", manhattan_distance)
    #solve_puzzle(puzzle, "m")
    #node = puzzle_node(puzzle, 3, 3, 2000)

    puzzle1 = [ [1,1,2], [3,7,5], [6,4,1]] #hammming distance = 4, manhattan distance = 8
    puzzle2 = [ [2,2,2], [3,7,5], [4,6,1]] #hammming distance = 4, manhattan distance = 8
    puzzle3 = [ [3,3,2], [7,3,5], [6,4,1]] #hammming distance = 4, manhattan distance = 8
    prioqueue  = PriorityQueue()
    prioqueue.push(puzzle1,900)
    prioqueue.push(puzzle2,200)
    prioqueue.push(puzzle3,200)
    print_puzzle(prioqueue.pop())

    print ("printing queue")
    while not prioqueue.isEmpty():
        state = prioqueue.pop()
        print_puzzle(state)


