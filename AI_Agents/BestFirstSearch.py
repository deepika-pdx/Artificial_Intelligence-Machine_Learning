import copy


class BestFirstSearch:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.max_steps = 2000
        self.reached_dict = {}

    @staticmethod
    def find_allowed_actions(node):
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
        return allowed_actions

    def generate_solution_path(self, node):
        print("Goal Reached")
        solution_node = node
        solution_path = ""
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
        return solution_path, no_of_steps

    def find_solution_using_heuristic(self, heuristic):
        pass

    def expand(self, node, frontier_queue, heuristic):
        pass
