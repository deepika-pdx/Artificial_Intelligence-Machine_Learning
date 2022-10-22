import random

from numpy import mean

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


# initial_state = [[1, 2, 3], [4, 'b', 5], [7, 8, 6]]
# initial_state = [[4, 3, 8], [2, 6, 1], ['b', 7, 5]]
# initial_state = [[3, 'b', 2], [4, 6, 8], [5, 1, 7]]

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 'b']]
path_array = []
path_steps_array = []
for i in range(1):
    are_puzzles_states_reachable = False

    while not are_puzzles_states_reachable:
        sample_initial_state = generate_random_8_puzzle()
        puzzle_parity = PuzzleParityCheck(sample_initial_state, goal_state)
        are_puzzles_states_reachable = puzzle_parity.compare_puzzle_parity()

    initial_state = sample_initial_state

    # Execute Greedy Best First Search Algorithm
    greedy_bfs = GreedyBestFirstSearch(initial_state, goal_state)
    solution_path, no_of_steps = greedy_bfs.find_solution_for_heuristic_1()
    path_array.append(solution_path)
    path_steps_array.append(no_of_steps)
    print("Solution path: " + solution_path)
    print("No. of steps in solution path: " + str(no_of_steps))

average_steps = mean(path_steps_array)
print("Average steps: " + str(average_steps))
