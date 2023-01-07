"""
function creates x puzzles, solves them and returns some statistics
"""

from eight_puzzle.create_puzzle import  *
from eight_puzzle.puzzle_functions import *
import timeit
import csv
def solve_x_puzzles(x):
    print(x)
# the defined goal state
    puzzle_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # hammming distance = 4, manhattan distance = 8

    puzzleArray = []
    # generate 100 puzzles
    starting_time = timeit.default_timer()
    # puzzle_ = create_random_puzzle()
    for y in range(0, x):
        puzzleArray.append(create_random_puzzle())
    generation_time = timeit.default_timer() - starting_time
    print("Time to generate", len(puzzleArray), "Puzzles:", generation_time)

    starting_time = timeit.default_timer()
    counter = 0
    expanded_nodes_avg = 0
    for y in range(0, x):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzleArray[y], puzzle_goal, "h")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes
    solve_time_hamming = timeit.default_timer() - starting_time
    print("Time to solve ", len(puzzleArray), "Puzzles using hamming distance:", solve_time_hamming)
    print("Average expanded nodes: ", expanded_nodes_avg / counter)
    expanded_nodes_avg_hamming = expanded_nodes_avg / counter
    print("Average solve time per puzzle : ", expanded_nodes_avg_hamming)

    counter = 0
    expanded_nodes_avg = 0
    starting_time = timeit.default_timer()
    for y in range(0, x):
        resolved_puzzle, expanded_nodes = solve_puzzle(puzzleArray[y], puzzle_goal, "m")
        counter += 1
        expanded_nodes_avg = expanded_nodes_avg + expanded_nodes

    solve_time_manhattan = timeit.default_timer() - starting_time
    print("Time to solve", len(puzzleArray), "Puzzles using manhattan distance:", solve_time_manhattan)
    expanded_nodes_avg_manhattan = expanded_nodes_avg / counter
    print("Average expanded nodes: ", expanded_nodes_avg_manhattan)

    #print as csv;
    print("number of puzzles; generation time; solve time hamming; solve time manhattan; avg expanded nodes hamming; avg expanded nodes manhattan; avg solve time hamming; avg solve time manhattan")
    print(x, ";", generation_time, ";",solve_time_hamming, ";",solve_time_manhattan, ";",expanded_nodes_avg_hamming, ";",expanded_nodes_avg_manhattan, ";" ,solve_time_hamming / x, ";", solve_time_manhattan/x)