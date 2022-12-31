#creates a puzzle using random values and returns the created puzzle as an 2d array.

#Sources:
#random number including range & choice: https://bobbyhadz.com/blog/python-generate-random-number-in-range-excluding-some-numbers

from random import choice
from eight_puzzle.puzzle_functions import print_puzzle

min_value = 1
max_value = 8
number_of_values = 8
debug = 1 # set to 1 and use in functions for additional debug outputs
def create_random_puzzle():
    puzzle = [ [0,0,0], [0,0,0], [0,0,0]]
    values = create_random_puzzle_values()    #create 8 random unique values
    #now its time to fill  the retrieved 8 values into the 2d array - position 0/0 stays always empty and will me omitted
    count = 0
    for x in range(3):
        for y in range(3):
            #print("counter", count)
            #puzzle[x][y] == values[count]
            if (x == 0 ) and (y == 0):
                puzzle [x][y] == 0
            else:
                puzzle [x][y] = values [count - 1] # puzzle has 9 slots / only 8 random values do exist
                #todo rewrite to generate the first random number with 0 and sijplyf this functionality
                # todo 0 must be included into random generation anyway!!!
            #    print (count)
            count = count + 1


    if debug:
        print_puzzle(puzzle)



def gen_random_number(min, max, exclude):
    return choice(
        [number for number in range(min, max)
         if number not in exclude]
    )

#generate 8 unique "random" numbers in a "random" order
def create_random_puzzle_values():
    values = []
    for i in range(min_value, max_value + 1): #+1 in order to create 8 "random" values
        values.append(gen_random_number(min_value, max_value + 1, values))
    if debug:
        print(values)
    return values

