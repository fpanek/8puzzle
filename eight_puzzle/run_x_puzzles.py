import timeit

from eight_puzzle.create_puzzle import *
from eight_puzzle.puzzle_functions import *


def solve_x_puzzles(x):

    """
    Creates the passed number of puzzles, solves them, and prints some statistical data.

    :param x: number of puzzles to create and solve
    :return: none
    """

    print("Creating", x, "puzzles...")
    puzzle_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    puzzle_array = []

    starting_time = timeit.default_timer()
    for y in range(0, x):
        puzzle_array.append(create_random_puzzle())

    generation_time = timeit.default_timer() - starting_time
    print("Time to generate", len(puzzle_array), "puzzles:", generation_time)
    print()

    starting_time = timeit.default_timer()
    counter = 0
    expanded_nodes_avg = 0
    for y in range(0, x):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzle_array[y], puzzle_goal, "h")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes

    print("******HAMMING******")

    solve_time_hamming = timeit.default_timer() - starting_time
    print("Time to solve", len(puzzle_array), "puzzles using Hamming distance:", solve_time_hamming)

    print("Average expanded nodes:", expanded_nodes_avg / counter)
    print("Average solve time per puzzle:", solve_time_hamming / x)

    counter = 0
    expanded_nodes_avg = 0
    starting_time = timeit.default_timer()
    for y in range(0, x):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzle_array[y], puzzle_goal, "m")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes

    print()
    print("******MANHATTAN******")

    solve_time_manhattan = timeit.default_timer() - starting_time
    print("Time to solve", len(puzzle_array), "puzzles using Manhattan distance:", solve_time_manhattan)

    print("Average expanded nodes:", expanded_nodes_avg / counter)
    print("Average solve time per puzzle:", solve_time_manhattan / x)
