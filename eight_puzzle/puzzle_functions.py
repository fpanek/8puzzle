import math as Math
import copy
from eight_puzzle.priority_queue import *
from eight_puzzle.puzzlenode import *

debug = 0


def print_puzzle(puzzle):

    """
    Prints the puzzle as a 3x3 field.

    :param puzzle: 2D array of puzzle values
    :return: none
    """

    print("Printed puzzle:")
    for x in range(3):
        for y in range(3):
            print(puzzle[x][y], end=" | ")
        print("")


def solve_puzzle(puzzle, puzzle_goal, method):

    """
    Solves the passed puzzle.

    :param puzzle: 2D array of puzzle values
    :param puzzle_goal: 2D array of puzzle values sorted in the solved order
    :param method: Hamming (h) or Manhattan (m) distance
    :return: Solved puzzle (array[]), number of expanded nodes (int), solve time (float)
    """

    open_list = PriorityQueue()
    closed_list = []

    node = PuzzleNode(puzzle, 0, calculate_heuristic_distance(puzzle, method))
    open_list.push(node, calculate_heuristic_distance(puzzle, method))

    walked_distance = 0
    expanded_nodes = 0

    while not open_list.is_empty():
        current_puzzle = open_list.pop()
        current_puzzle_grid = current_puzzle.puzzle

        # return solved puzzle if solution found
        if current_puzzle_grid == puzzle_goal:
            return current_puzzle_grid, expanded_nodes

        # check possible moves
        possible_moves, x, y = check_possible_moves(current_puzzle_grid)

        # execute possible moves
        for i in possible_moves:
            try_move = move_empty_tile(current_puzzle_grid, i, x, y)
            expanded_nodes += 1
            if try_move not in closed_list:
                closed_list.append(try_move)  # add new node to examined nodes
                # (self, puzzle, g, h, parent_node)
                heuristic_distance = calculate_heuristic_distance(try_move, method)
                walked_distance += 1  # moved one tile
                open_list.push(PuzzleNode(try_move, walked_distance, heuristic_distance), heuristic_distance)


def check_possible_moves(puzzle):

    """
    Checks if a move in a certain direction is possible.

    Directions:
        * 1 = left
        * 2 = up
        * 3 = right
        * 4 = down
    :param puzzle: 2D array of puzzle values
    :return: list of directions a tile can be moved in, index of the empty tile
    """

    possible_moves = []
    x, y = find_tile_position(puzzle, 0)

    # check for left
    if 1 <= y <= 2:
        # move left possible
        possible_moves.append(1)
        # print("move left possible:", x, y)

    # check for up:
    if 1 <= x <= 2:
        # move up possible
        possible_moves.append(2)
        # print("move up possible:", x, y)

    # check for right:
    if 1 >= y >= 0:
        # move right possible
        # print("move right possible:", x, y)
        possible_moves.append(3)

    # check for down:
    if 1 >= x >= 0:
        # move down possible
        possible_moves.append(4)
        # print("move down possible:", x, y)

    return possible_moves, x, y


def find_tile_position(puzzle, tile_value):

    """
    Finds the position index of a tile value within the puzzle array.

    :param puzzle: 2D array of puzzle values
    :param tile_value: number to find (e.g. 0)
    :return: row and column index of the tile (int)
    """

    x_found = 0
    y_found = 0
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] == tile_value:
                x_found = x
                y_found = y
    return x_found, y_found


def move_empty_tile(puzzle, direction, x, y):

    """
    Moves the empty (0 value) tile of a puzzle in a corresponding direction.

    Directions:
        * 1 = left
        * 2 = up
        * 3 = right
        * 4 = down
    :param puzzle: 2D array of values
    :param direction: direction for moving (int)
    :param x: row index (int)
    :param y: column index (int)
    :return: Updated puzzle with the empty tile in a new position (array)
    """

    x, y = x, y
    old_tile_value = 0
    new_puzzle = copy.deepcopy(puzzle)
    match direction:
        case 1:  # left
            old_tile_value = new_puzzle[x][y - 1]
            new_puzzle[x][y - 1] = 0
        case 2:  # up
            old_tile_value = new_puzzle[x - 1][y]
            new_puzzle[x - 1][y] = 0
        case 3:  # right
            old_tile_value = new_puzzle[x][y + 1]
            new_puzzle[x][y + 1] = 0
        case 4:  # down
            old_tile_value = new_puzzle[x + 1][y]
            new_puzzle[x + 1][y] = 0
    new_puzzle[x][y] = old_tile_value
    return new_puzzle


def calculate_heuristic_distance(puzzle, method):

    """
    Calculates the heuristic distance of a puzzle.

    Calls the corresponding method of distance calculation.
    :param puzzle: 2D array of puzzle values
    :param method: Hamming (h) or Manhattan (m) distance
    :return: Calculated distance (int)
    """

    heuristic_distance = 0
    match method:
        case "h":
            heuristic_distance = calculate_hamming_distance(puzzle)
        case "m":
            heuristic_distance = calculate_manhattan_distance(puzzle)
    return heuristic_distance


def calculate_manhattan_distance(puzzle):

    """
    Calculates the **Manhattan** distance of a given puzzle:

    *Sum of the vertical and horizontal distances from each tile to their goal position.*

    Checks if the position of each tile in a puzzle corresponds to the expected result (solved puzzle).
    If the value is in the wrong position, looks for the correct position and calculates the way
    to get the tile in the correct place.

    Returns the **absolute positive value**.

    :param puzzle: 2D array of puzzle values
    :return: Manhattan distance (int)
    """

    final_state_puzzle = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    distance = 0
    x_found = 0
    y_found = 0
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] != final_state_puzzle[x][y]:
                value = puzzle[x][y]
                for xx in range(3):
                    for yy in range(3):
                        if final_state_puzzle[xx][yy] == value:
                            x_found = xx
                            y_found = yy
                distance += Math.fabs(x_found - x) + Math.fabs(y_found - y)
    return distance


def calculate_hamming_distance(puzzle):

    """
    Calculates the **Hamming distance** of a given puzzle:

    *Number of tiles not in their goal position*

    0 (empty tile) is **excluded**.

    :param puzzle: 2D array of puzzle values
    :return: Hamming distance (int)
    """

    distance = 0
    final_value = 0
    for x in range(3):
        for y in range(3):
            if puzzle[x][y] != 0 and puzzle[x][y] != final_value:
                distance += 1
            final_value += 1
    return distance


def valid_move(x, y):

    """
    Checks if a move is valid by checking if the position index lies within the boundaries of the game.

    :param x: column index
    :param y: row index
    :return: valid or invalid (boolean)
    """

    if x <= 3 and y <= 3:
        return True
    else:
        return False


def is_solvable(puzzle):

    """
    Checks if a puzzle is solvable or not.

    A puzzle is not solvable if the number of inversions in the input state is odd.
    :param puzzle: 2D array of puzzle values
    :return: solvable or not solvable (boolean)
    """

    count = 0
    for x in range(0, 9):
        for y in range(x+1, 9):
            if puzzle[y] != 0 and puzzle[x] != 0 and puzzle[x] > puzzle[y]:
                count += 1
    if count % 2 == 0:
        solvable = True
    else:
        solvable = False

    if debug:
        if solvable:
            print("Puzzle is solvable")
        else:
            print("Puzzle is not solvable")
    return solvable
