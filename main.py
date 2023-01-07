from eight_puzzle.create_puzzle import  *
from eight_puzzle.puzzle_functions import *
import timeit

#definition of puzzle - 2d array
#     0 1 2 (col Axis - second value of array)
#  0 |0|1|2|
#  1 |3|4|5|
#  2 |6|7|8|
#  (row Axis first value of the array)

if __name__ == '__main__':

    # the defined goal state
    puzzle_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # hammming distance = 4, manhattan distance = 8

    """
    Tests using tst data
    puzzleArray = []
    puzzleArray.append([[0, 8, 2], [3, 7, 5], [6, 4, 1]])  # hammming distance = 4, manhattan distance = 8
    puzzleArray.append([[3, 8, 0], [5, 4, 1], [7, 6, 2]])
    puzzleArray.append([[0, 2, 3], [1, 7, 8], [5, 6, 4]])

    for x in puzzleArray:
        print("solving puzzle: ", x)
        print("unsorted field:")
        print_puzzle(x)
        resolved_puzzle, expanded_nodes = solve_puzzle(x, puzzle_goal, "h")
        print("sorted field:")
        print_puzzle(resolved_puzzle)
        print(expanded_nodes)
    """

    puzzleArray = []
    #generate 100 puzzles
    starting_time = timeit.default_timer()
    #puzzle_ = create_random_puzzle()
    for x in range(0,100):
        puzzleArray.append(create_random_puzzle())
    print("Time to generate", len(puzzleArray), "Puzzles:", timeit.default_timer() - starting_time)


    starting_time = timeit.default_timer()
    counter = 0
    expanded_nodes_avg = 0
    for x in range(0, 100):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzleArray[x], puzzle_goal, "h")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes
    print("Time to solve ", len(puzzleArray), "Puzzles using hamming distance:", timeit.default_timer() - starting_time)
    print("Average expanded nodes: ", expanded_nodes_avg/counter)

    counter = 0
    expanded_nodes_avg = 0
    starting_time = timeit.default_timer()
    for x in range(0, 100):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzleArray[x], puzzle_goal, "m")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes
    print("Time to solve", len(puzzleArray), "Puzzles using manhattan distance:", timeit.default_timer() - starting_time)
    print("Average expanded nodes: ", expanded_nodes_avg/counter)








