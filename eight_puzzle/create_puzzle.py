#creates a puzzle using random values and returns the created puzzle as an 2d array.

#Sources:
#random number including range & choice: https://bobbyhadz.com/blog/python-generate-random-number-in-range-excluding-some-numbers

from random import choice
from eight_puzzle.puzzle_functions import print_puzzle,is_solvable

min_value = 0
max_value = 8
number_of_values = 9
debug =  1# set to 1 and use in functions for additional debug outputs
def create_random_puzzle():
    puzzle = [ [0,0,0], [0,0,0], [0,0,0]]
    values = create_random_puzzle_values()    #create 9 random unique values
    #now its time to fill  the retrieved 8 values into the 2d array - position 0/0 stays always empty and will me omitted
    count = 0
    for x in range(3):
        for y in range(3):
            puzzle[x][y] = values[count]
            count += 1
    if debug:
        print_puzzle(puzzle)
    return puzzle


def gen_random_number(min, max, exclude):
    return choice(
        [number for number in range(min, max)
         if number not in exclude]
    )


#generate 9 unique "random" numbers in a "random" order
#verifies if puzzle is solvable
def create_random_puzzle_values():
    solvable = False
    while (solvable == False): #generate new puzzle until one is solvable
        values = []
        for i in range(min_value, max_value + 1): #+1 in order to create 8 "random" values
            values.append(gen_random_number(min_value, max_value + 1, values))
        if debug:
            print(values)
        solvable = is_solvable(values)
        if (solvable == True):
            if debug:
                print("Puzzle is solvable, returning values")
        else:
            if debug:
                print("Puzzle is not solvable, generating new values...")
    return values

