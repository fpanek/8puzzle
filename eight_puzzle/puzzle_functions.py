#provides different functionalities of the puzzle
# is it solvable?
# input value: puzzle as 2d array
debug = 1



import math as Math
import copy
from eight_puzzle.priority_queue import *
from eight_puzzle.puzzle_node import *


from heapq import heappush, heappop

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
def solve_puzzle(puzzle,puzzle_goal, method):
    #TODO check for solvability e.g if function is used to solve non solvable puzzle
    openList = PriorityQueue()
    node = puzzle_node(puzzle, 0, 0, 0)
    openList.push(node,0)
    closedList = []

    while not openList.isEmpty():
        #puzzle = openList.pop().puzzle
        #print(puzzle)
        #if puzzle == puzzle_goal:
        #    return puzzle
        #closedList.append(puzzle)

        current_puzzle = openList.pop().puzzle
        if current_puzzle == puzzle_goal:
            return current_puzzle

        #check possible moves
        #moves are 1=left,2=up,3=right,4=down
        possible_moves = check_possible_moves(current_puzzle)

        #execute possible moves
        for i in possible_moves:
            print("test")
            try_move = move_empty_tile(puzzle,i)
            if try_move not in closedList:
                closedList.append(try_move) #add new node to examined nodes
                openList.push(puzzle_node(puzzle, 0, 0, 0), 0)#add new node to heap #TODO 0,0,0,0 set correct values h/g/n
            else:
                print("deleting node required?")

        #calculate heuristic distance for possible moves

        #if the path to the neighbor is better than the previos one save it

        #if the neighbor is not in openset add it to list





#moves are 1=left,2=up,3=right,4=down
def check_possible_moves(puzzle):
    possible_moves = []
    x,y = find_tile_position(puzzle, 0)
    #check for left
    if y>= 1 and y<=2:
        #move left possible
        possible_moves.append(1)
    #check for up:
    if x>= 1 and x<=2:
        #move up possible
        possible_moves.append(2)
    #check for right:
    if y<=1 and y>=0:
        #move right possible
        possible_moves.append(3)
    #check for down:
    if x<=1 and x>=0:
        #move down possible
        possible_moves.append(4)
    return possible_moves


#find tile (e.g. 0 for empty tile) and return position
def find_tile_position(puzzle,tile_value):
    xFound = 0
    yFound = 0
    for x in range(3):
        for y in range(3):
            #print("current value:", puzzle[x][y])
            if puzzle[x][y] == tile_value:
                xFound = x
                yFound = y
    return xFound, yFound



#TODO
#moves are 1=left,2=up,3=right,4=down
def move_empty_tile(puzzle, direction):
    print("todo")
    new_puzzle = copy.deepcopy(puzzle)
    x,y = find_tile_position(new_puzzle, 0)
    match direction:
        case 1:
            new_tile = new_puzzle[x][y-1]
            new_puzzle[x][y - 1] = 0
        case 2:
            new_tile = new_puzzle[x+1][y]
            new_puzzle[x][y - 1] = 0
        case 3:
            new_tile = new_puzzle[x][y+1]
            new_puzzle[x][y - 1] = 0
        case 4:
            new_tile = new_puzzle[x-1][y]
            new_puzzle[x][y - 1] = 0
    new_puzzle[x][y] = new_tile
    return new_puzzle

#calculates the heuristic distance
#puzzle = 8 puzzle 2d array
#method = h or m (hamming or manhattan)
def calculate_heuristic_distance(puzzle, method):
    match method:
        case "h":
            heuristic_distance = calculate_hamming_distance(puzzle)
        case "m":
            heuristic_distance = calculate_manhattan_distance(puzzle)
    return heuristic_distance

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
                distance += Math.fabs(xFound-x) + Math.fabs(yFound-y) #calculate the required way to get the tile in the correct order / fabs = return the absolute positive value
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


#returns true if move is valid / within the boundaries of the game
def valid_move(x,y):
    if x <= 3 and y <= 3:
        return True
    else:
        return False


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



