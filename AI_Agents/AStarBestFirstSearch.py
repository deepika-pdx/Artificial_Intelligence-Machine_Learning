import copy
from queue import PriorityQueue

from AI_Agents.BestFirstSearch import BestFirstSearch
from AI_Agents.PuzzleHeuristics import PuzzleHeuristics
from AI_Agents.PuzzleNode import PuzzleNode


class AStarBestFirstSearch(BestFirstSearch):

    def expand(self, node, frontier_queue, heuristic):
        self.reached_dict.update({str(node.state): node})
        actions = BestFirstSearch.find_allowed_actions(node)

        for action in actions:
            if action == "Left":
                new_node_state_left = copy.deepcopy(node.state)
                is_node_state_created = False
                for i in range(len(new_node_state_left)):
                    for j in range(len(new_node_state_left)):
                        if new_node_state_left[i][j] == 'b':
                            temp = new_node_state_left[i][j - 1]
                            new_node_state_left[i][j - 1] = 'b'
                            new_node_state_left[i][j] = temp

                            left_node_path_cost = node.path_cost + 1
                            new_node_left = PuzzleNode(new_node_state_left, node, action, left_node_path_cost)
                            new_node_heuristic_left = PuzzleHeuristics(new_node_state_left, self.goal_state)
                            if heuristic == "1":
                                new_node_evaluation_fn_left = left_node_path_cost + new_node_heuristic_left.no_of_misplaced_tiles()
                            elif heuristic == "2":
                                new_node_evaluation_fn_left = left_node_path_cost + new_node_heuristic_left.sum_of_tile_manhatten_distances()
                            elif heuristic == "3":
                                misplaced_tiles_count_left = new_node_heuristic_left.no_of_misplaced_tiles()
                                tiles_m_distance_left = new_node_heuristic_left.sum_of_tile_manhatten_distances()
                                new_node_evaluation_fn_left = max(misplaced_tiles_count_left, tiles_m_distance_left)
                            frontier_queue.put((new_node_evaluation_fn_left, new_node_left))

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

                            right_node_path_cost = node.path_cost + 1
                            new_node_right = PuzzleNode(new_node_state_right, node, action, right_node_path_cost)
                            new_node_heuristic_right = PuzzleHeuristics(new_node_state_right, self.goal_state)
                            if heuristic == "1":
                                new_node_evaluation_fn_rt = right_node_path_cost + new_node_heuristic_right.no_of_misplaced_tiles()
                            elif heuristic == "2":
                                new_node_evaluation_fn_rt = right_node_path_cost + new_node_heuristic_right.sum_of_tile_manhatten_distances()
                            elif heuristic == "3":
                                misplaced_tiles_count_rt = new_node_heuristic_right.no_of_misplaced_tiles()
                                tiles_m_distance_rt = new_node_heuristic_right.sum_of_tile_manhatten_distances()
                                new_node_evaluation_fn_rt = max(misplaced_tiles_count_rt, tiles_m_distance_rt)
                            frontier_queue.put((new_node_evaluation_fn_rt, new_node_right))

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

                            up_node_path_cost = node.path_cost + 1
                            new_node_up = PuzzleNode(new_node_state_up, node, action, up_node_path_cost)
                            new_node_heuristic_up = PuzzleHeuristics(new_node_state_up, self.goal_state)
                            if heuristic == "1":
                                new_node_evaluation_fn_up = up_node_path_cost + new_node_heuristic_up.no_of_misplaced_tiles()
                            elif heuristic == "2":
                                new_node_evaluation_fn_up = up_node_path_cost + new_node_heuristic_up.sum_of_tile_manhatten_distances()
                            elif heuristic == "3":
                                misplaced_tiles_count_up = new_node_heuristic_up.no_of_misplaced_tiles()
                                tiles_m_distance_up = new_node_heuristic_up.sum_of_tile_manhatten_distances()
                                new_node_evaluation_fn_up = max(misplaced_tiles_count_up, tiles_m_distance_up)
                            frontier_queue.put((new_node_evaluation_fn_up, new_node_up))

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

                            down_node_path_cost = node.path_cost + 1
                            new_node_down = PuzzleNode(new_node_state_down, node, action, down_node_path_cost)
                            new_node_heuristic_down = PuzzleHeuristics(new_node_state_down, self.goal_state)
                            if heuristic == "1":
                                mis = new_node_heuristic_down.no_of_misplaced_tiles()
                                new_node_evaluation_fn_down = down_node_path_cost + new_node_heuristic_down.no_of_misplaced_tiles()
                            elif heuristic == "2":
                                new_node_evaluation_fn_down = down_node_path_cost + new_node_heuristic_down.sum_of_tile_manhatten_distances()
                            elif heuristic == "3":
                                misplaced_tiles_count_down = new_node_heuristic_down.no_of_misplaced_tiles()
                                tiles_m_distance_down = new_node_heuristic_down.sum_of_tile_manhatten_distances()
                                new_node_evaluation_fn_down = max(misplaced_tiles_count_down, tiles_m_distance_down)
                            frontier_queue.put((new_node_evaluation_fn_down, new_node_down))

                            is_node_state_created = True
                            break
                    if is_node_state_created:
                        break

    def find_solution_using_heuristic(self, heuristic):
        path_cost = 0
        puzzle_initial_node = PuzzleNode(self.initial_state, "", "", path_cost)
        puzzle_heuristic = PuzzleHeuristics(puzzle_initial_node.state, self.goal_state)

        if heuristic == "1":
            queue_key = path_cost + puzzle_heuristic.no_of_misplaced_tiles()
        elif heuristic == "2":
            queue_key = path_cost + puzzle_heuristic.sum_of_tile_manhatten_distances()
        elif heuristic == "3":
            misplaced_tiles_count = puzzle_heuristic.no_of_misplaced_tiles()
            tiles_m_distance = puzzle_heuristic.sum_of_tile_manhatten_distances()
            queue_key = max(misplaced_tiles_count, tiles_m_distance)
        frontier_queue = PriorityQueue()
        frontier_queue.put((queue_key, puzzle_initial_node))

        no_of_moves = 0
        while frontier_queue.qsize() != 0 or no_of_moves != self.max_steps:
            node_tuple = frontier_queue.get()
            state_string = str(node_tuple[1].state)
            while state_string in self.reached_dict:
                node_tuple = frontier_queue.get()
                state_string = str(node_tuple[1].state)

            # Heuristic measure holds the no of misplaced tiles when using heuristic 1 and
            # it holds the sum of manhatten distances of the tiles when using heuristis 2
            heuristic_measure = node_tuple[0]
            node = node_tuple[1]
            no_of_moves += 1
            goal_state_string = str(self.goal_state)
            if state_string == goal_state_string:
                solution_path, no_of_steps = super().generate_solution_path(node)
                break
            else:
                self.expand(node, frontier_queue, heuristic)
        return solution_path, no_of_steps
