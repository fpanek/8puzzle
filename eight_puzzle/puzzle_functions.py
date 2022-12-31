#provides different functionalities of the puzzle
# is it solvable?
# input value: puzzle as 2d array


def print_puzzle(puzzle):
    print("Printing field..")
    for x in range (3):
        for y in range (3):
            print(puzzle[x][y], end = " | " )
        print("")


