#provides different functionalities of the puzzle
# is it solvable?
# input value: puzzle as 2d array
debug = 0

def print_puzzle(puzzle):
    print("Printing field..")
    for x in range (3):
        for y in range (3):
            print(puzzle[x][y], end = " | " )
        print("")


#usefule lecutre?
#https://www.cs.princeton.edu/courses/archive/spr13/cos226/assignments/8puzzle.html

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

#check if the puzzle is solvable - return true if yes / false if it is not solvable
#puzzle is expected in form of an 1d array
#criteria: "It is not possible to solve an instance of 8 puzzle if number of inversions is odd in the input state. " (source: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/)
def is_solvable(puzzle):
    count = 0
    for x in range(0,9):
        for y in range (x+1, 9):
            if puzzle[y] != 0 and puzzle[x] != 0 and puzzle[x] > puzzle[y]:
                count += 1
    if (count % 2 == 0):
        solvable = True
    else:
        solvable = False
    if debug:
        if (solvable == True):
            print("puzzle is solvable")
        else:
            print("puzzle is not solvable")
    return solvable



