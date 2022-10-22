import random
from functools import total_ordering


@total_ordering
class PuzzleNode:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.number = random.random()

    # Added due to issue in adding multiple PuzzleNode objects to the frontier_queue.
    # I referred 'https://stackoverflow.com/questions/43477958/typeerror-not-supported-between-instances-python'
    # for fixing this issue
    def __lt__(self, other):
        return self.number < other.number
