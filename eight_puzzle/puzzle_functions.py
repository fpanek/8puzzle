#provides different functionalities of the puzzle
# is it solvable?
# input value: puzzle as 2d array


def print_puzzle(puzzle):
    print("Printing field..")
    for x in range (3):
        for y in range (3):
            print(puzzle[x][y], end = " | " )
        print("")



#solve puzzle
# required Parameters: puzzle (2d array), method to solve (hamming/manhattan = h or m),
# returns: solved puzzle, number of expanded nodes, solve time

def solve_puzzle(puzzle, method):
    print("todo")
    return puzzle, expanded_nodes, solve_time


def solve_puzzle_hamming():
    print("todo")


def solve_puzzle_manhattan():
    print("todo")
