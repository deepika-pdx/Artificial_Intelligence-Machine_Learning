import random

from numpy import mean

from AI_Agents.AStarBestFirstSearch import AStarBestFirstSearch
from AI_Agents.GreedyBestFirstSearch import GreedyBestFirstSearch
from AI_Agents.PuzzleParityCheck import PuzzleParityCheck


def generate_random_tile_number(num_array, n):
    if n == 0:
        return num_array[0]
    return num_array[random.randint(0, n)]


def generate_random_8_puzzle():
    puzzle = []
    number_array = [1, 2, 3, 4, 5, 6, 7, 8, 'b']
    n = 8
    for i in range(3):
        puzzle.append([])
        for j in range(1, 4):
            tile_number = generate_random_tile_number(number_array, n)
            puzzle[i].append(tile_number)
            number_array.remove(tile_number)
            n -= 1
    print(puzzle)
    return puzzle


def generate_random_15_puzzle():
    puzzle = []
    number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'b']
    n = 15
    for i in range(4):
        puzzle.append([])
        for j in range(1, 5):
            tile_number = generate_random_tile_number(number_array, n)
            puzzle[i].append(tile_number)
            number_array.remove(tile_number)
            n -= 1
    print(puzzle)
    return puzzle


def find_reachable_initial_state(final_state, puzzle_size):
    are_puzzles_states_reachable = False

    while not are_puzzles_states_reachable:
        if puzzle_size == 8:
            sample_initial_state = generate_random_8_puzzle()
        elif puzzle_size == 15:
            sample_initial_state = generate_random_15_puzzle()
        puzzle_parity = PuzzleParityCheck(sample_initial_state, final_state)
        are_puzzles_states_reachable = puzzle_parity.compare_puzzle_parity()

    return sample_initial_state


input_puzzle_size = 15
if input_puzzle_size == 8:
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'b']]
elif input_puzzle_size == 15:
    goal_state = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15, 'b']]

heuristics = ["1", "2", "3"]
# Heuristic "1" : No of misplaced tiles
# Heuristic "2" : Sum of Manhatten distances of each tile
# Heuristic "3" : Max of (No of misplaced tiles, Sum of Manhatten distances of tiles)
for p_heuristic in heuristics:

    path_array_greedy_bfs = []
    path_steps_array_greedy_bfs = []

    path_array_astar_bfs = []
    path_steps_array_star_bfs = []

    for k in range(5):
        initial_state = find_reachable_initial_state(goal_state, input_puzzle_size)
        heuristic = p_heuristic

        # Execute Greedy Best First Search Algorithm using heuristic
        greedy_bfs = GreedyBestFirstSearch(initial_state, goal_state)
        solution_path_greedy_bfs, no_of_steps_greedy_bfs = greedy_bfs.find_solution_using_heuristic(heuristic)
        path_array_greedy_bfs.append(solution_path_greedy_bfs)
        path_steps_array_greedy_bfs.append(no_of_steps_greedy_bfs)
        print("Solution path for Greedy BFS: " + solution_path_greedy_bfs)
        print("No. of steps in solution path of Greedy BFS: " + str(no_of_steps_greedy_bfs))

        # Execute A* Best First Search Algorithm using heuristic
        astar_bfs = AStarBestFirstSearch(initial_state, goal_state)
        solution_path_astar_bfs, no_of_steps_astar_bfs = astar_bfs.find_solution_using_heuristic(heuristic)
        path_array_astar_bfs.append(solution_path_astar_bfs)
        path_steps_array_star_bfs.append(no_of_steps_astar_bfs)
        print("Solution path for A* BFS: " + solution_path_astar_bfs)
        print("No. of steps in solution path of A* BFS: " + str(no_of_steps_astar_bfs))

    average_steps_greedy_bfs = mean(path_steps_array_greedy_bfs)
    print("Average steps in solution path using Greedy BFS: " + str(average_steps_greedy_bfs))
    average_steps_astar_bfs = mean(path_steps_array_star_bfs)
    print("Average steps in solution path using A* BFS: " + str(average_steps_astar_bfs))
