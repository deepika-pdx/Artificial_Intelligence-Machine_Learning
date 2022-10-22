import copy
from queue import PriorityQueue

import numpy as np

from AI_Agents.PuzzleHeuristics import PuzzleHeuristics
from AI_Agents.PuzzleNode import PuzzleNode


class GreedyBestFirstSearch:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.max_steps = 10000
        self.reached_dict = {}

    def expand(self, node, path_cost, frontier_queue):
        self.reached_dict.update({str(node.state): node})
        allowed_actions = []
        node_state = copy.deepcopy(node.state)
        for i in range(len(node_state)):
            for j in range(len(node_state)):
                if i == j == 0 and node_state[i][j] == 'b':
                    allowed_actions = ["Right", "Down"]
                elif i == 0 and j == 1 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Right", "Down"]
                elif i == 0 and j == 2 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Down"]
                elif i == 1 and j == 0 and node_state[i][j] == 'b':
                    allowed_actions = ["Up", "Right", "Down"]
                elif i == 1 and j == 1 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Right", "Up", "Down"]
                elif i == 1 and j == 2 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Up", "Down"]
                elif i == 2 and j == 0 and node_state[i][j] == 'b':
                    allowed_actions = ["Right", "Up"]
                elif i == 2 and j == 1 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Right", "Up"]
                elif i == 2 and j == 2 and node_state[i][j] == 'b':
                    allowed_actions = ["Left", "Up"]

        for action in allowed_actions:
            if action == "Left":
                new_node_state_left = copy.deepcopy(node.state)
                is_node_state_created = False
                for i in range(len(new_node_state_left)):
                    for j in range(len(new_node_state_left)):
                        if new_node_state_left[i][j] == 'b':
                            temp = new_node_state_left[i][j - 1]
                            new_node_state_left[i][j - 1] = 'b'
                            new_node_state_left[i][j] = temp
                            new_node_left = PuzzleNode(new_node_state_left, node, action, path_cost)
                            new_node_heuristic_left = PuzzleHeuristics(new_node_state_left, self.goal_state)
                            new_node_evaluation_function_left = new_node_heuristic_left.no_of_misplaced_tiles()
                            frontier_queue.put((new_node_evaluation_function_left, new_node_left))
                            is_node_state_created = True
                            break
                    if is_node_state_created:
                        break
            elif action == "Right":
                new_node_state_right = copy.deepcopy(node.state)
                is_node_state_created = False
                for i in range(len(new_node_state_right)):
                    for j in range(len(new_node_state_right)):
                        if new_node_state_right[i][j] == 'b':
                            temp = new_node_state_right[i][j + 1]
                            new_node_state_right[i][j + 1] = 'b'
                            new_node_state_right[i][j] = temp
                            new_node_right = PuzzleNode(new_node_state_right, node, action, path_cost)
                            new_node_heuristic_right = PuzzleHeuristics(new_node_state_right, self.goal_state)
                            new_node_evaluation_function_right = new_node_heuristic_right.no_of_misplaced_tiles()
                            frontier_queue.put((new_node_evaluation_function_right, new_node_right))
                            is_node_state_created = True
                            break
                    if is_node_state_created:
                        break
            elif action == "Up":
                new_node_state_up = copy.deepcopy(node.state)
                is_node_state_created = False
                for i in range(len(new_node_state_up)):
                    for j in range(len(new_node_state_up)):
                        if new_node_state_up[i][j] == 'b':
                            temp = new_node_state_up[i - 1][j]
                            new_node_state_up[i - 1][j] = 'b'
                            new_node_state_up[i][j] = temp
                            new_node_up = PuzzleNode(new_node_state_up, node, action, path_cost)
                            new_node_heuristic_up = PuzzleHeuristics(new_node_state_up, self.goal_state)
                            new_node_evaluation_function_up = new_node_heuristic_up.no_of_misplaced_tiles()
                            frontier_queue.put((new_node_evaluation_function_up, new_node_up))
                            is_node_state_created = True
                            break
                    if is_node_state_created:
                        break
            elif action == "Down":
                new_node_state_down = copy.deepcopy(node.state)
                is_node_state_created = False
                for i in range(len(new_node_state_down)):
                    for j in range(len(new_node_state_down)):
                        if new_node_state_down[i][j] == 'b':
                            temp = new_node_state_down[i + 1][j]
                            new_node_state_down[i + 1][j] = 'b'
                            new_node_state_down[i][j] = temp
                            new_node_down = PuzzleNode(new_node_state_down, node, action, path_cost)
                            new_node_heuristic_down = PuzzleHeuristics(new_node_state_down, self.goal_state)
                            new_node_evaluation_function_down = new_node_heuristic_down.no_of_misplaced_tiles()
                            frontier_queue.put((new_node_evaluation_function_down, new_node_down))
                            is_node_state_created = True
                            break
                    if is_node_state_created:
                        break

    def find_solution_for_heuristic_1(self):
        puzzle_initial_node = PuzzleNode(self.initial_state, "", "", 0)
        puzzle_heuristic = PuzzleHeuristics(puzzle_initial_node.state, self.goal_state)
        frontier_queue = PriorityQueue()
        frontier_queue.put((puzzle_heuristic.no_of_misplaced_tiles(), puzzle_initial_node))

        no_of_moves = 0
        path_cost = 0
        goal_state_node = puzzle_initial_node
        while frontier_queue.qsize() != 0 or no_of_moves != self.max_steps:
            node_tuple = frontier_queue.get()
            state_string = str(node_tuple[1].state)
            while state_string in self.reached_dict:
                node_tuple = frontier_queue.get()
                state_string = str(node_tuple[1].state)

            no_of_misplaced_tiles = node_tuple[0]
            node = node_tuple[1]

            no_of_moves += 1
            path_cost += 1
            if no_of_misplaced_tiles == 0:
                goal_state_node = node
                print("Goal Reached")
                solution_node = goal_state_node
                solution_path = ""
                start = True
                no_of_steps = 0
                while solution_node.parent != "":
                    temp_string = ""
                    for row in solution_node.state:
                        for tile in row:
                            temp_string = temp_string + str(tile) + " "

                    solution_node = solution_node.parent
                    solution_path = "(" + temp_string + ")" + "--->" + solution_path
                    no_of_steps += 1

                # Add initial state at the end
                temp_string = ""
                for row in self.initial_state:
                    for tile in row:
                        temp_string = temp_string + str(tile) + " "
                solution_path = "(" + temp_string + ")" + "--->" + solution_path
                solution_path = solution_path[:-4]
                no_of_steps += 1
                break
            else:
                self.expand(node, path_cost, frontier_queue)
        return solution_path, no_of_steps
