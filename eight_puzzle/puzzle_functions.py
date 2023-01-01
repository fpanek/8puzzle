#provides different functionalities of the puzzle
# is it solvable?
# input value: puzzle as 2d array
debug = 1

import math as Math

def print_puzzle(puzzle):
    print("Printing field..")
    for x in range (3):
        for y in range (3):
            print(puzzle[x][y], end = " | " )
        print("")


#usefule lecutre?
#https://www.cs.princeton.edu/courses/archive/spr13/cos226/assignments/8puzzle.html
#Hamming Distance: The number of tiles not in their goal position.
#Manhattan Distance: The sum of the vertical and horizontal distances from each tile to their goal position.


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


def calculate_manhattan_distance(puzzle):
    finalStatePuzzle = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    distance = 0
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] != finalStatePuzzle[x][y]:  #value is not on the position as expected
                #Find expected position
                value = puzzle[x][y]
                for xx in range(3):
                    for yy in range(3):
                        if finalStatePuzzle[xx][yy] == value:
                            xFound = xx
                            yFound = yy
                distance += Math.fabs(xFound-x) + Math.fabs(yFound-y)
    return distance


#the number of tiles not in their goal position - 0 (=empty tile) is excluded
def calculate_hamming_distance(puzzle):
    distance = 0
    finalValue = 0
    for x in range (3):
        for y in range (3):
            if puzzle[x][y] != 0 and puzzle[x][y] != finalValue:
                distance += 1
            finalValue += 1
    return distance


#check if the puzzle is solvable - return true if yes / false if it is not solvable
#puzzle is expected in form of an 1d array
#criteria: "It is not possible to solve an instance of 8 puzzle if number of inversions is odd in the input state. " (source: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/)
def is_solvable(puzzle):
    count = 0
    for x in range(0,9):
        for y in range (x+1, 9): #TODO why x+1? explain?!
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



