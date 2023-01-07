from random import choice
from eight_puzzle.puzzle_functions import print_puzzle, is_solvable

min_value = 0
max_value = 8
number_of_values = 9
debug = 0  # Set to 1 and use in functions for additional debug outputs


def create_random_puzzle():
    """
    Creates an 8 puzzle with generated random values.

    | 0 | 1 | 2 |

    | 3 | 4 | 5 |

    | 6 | 7 | 8 |

    Row index = first value in array (x)

    Column index = second value in array (y)

    :return: puzzle as a 2D array of 9 random values
    """

    puzzle = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    values = create_random_puzzle_values()
    count = 0
    for x in range(3):
        for y in range(3):
            puzzle[x][y] = values[count]
            count += 1
    if debug:
        print_puzzle(puzzle)
    return puzzle


def gen_random_number(min_num, max_num, exclude):

    """
    Generates a random number in a given range.

    :param min_num: smallest value (int)
    :param max_num: biggest value (int)
    :param exclude: list of numbers to be excluded (int)
    :return: random number (int)
    """

    return choice(
        [number for number in range(min_num, max_num)
         if number not in exclude]
    )


def create_random_puzzle_values():

    """
    Creates an array of values for a new puzzle.

    Calls the method ``gen_random_number()`` nine times, each time excluding already used numbers,
    and saves them in an array.

    Checks if the puzzle with created values can be solved. If not, generates new nine numbers again.
    :return: List of puzzle values that are solvable
    """

    solvable = False
    values = []
    while not solvable:
        for i in range(min_value, max_value + 1):
            values.append(gen_random_number(min_value, max_value+1, values))
        if debug:
            print(values)
        solvable = is_solvable(values)

        if solvable:
            if debug:
                print("Puzzle is solvable, returning values")
        else:
            values = []
            if debug:
                print("Puzzle is not solvable, generating new values...")
    return values
