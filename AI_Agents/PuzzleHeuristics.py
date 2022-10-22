class PuzzleHeuristics:
    def __init__(self, current_state, goal_state):
        current_state_array = []
        for row in current_state:
            for tile in row:
                current_state_array.append(tile)
        self.current_state_array = current_state_array

        goal_state_array = []
        for row in goal_state:
            for tile in row:
                goal_state_array.append(tile)
        self.goal_state_array = goal_state_array

    def no_of_misplaced_tiles(self):
        misplaced_tiles_count = 0

        index = 0
        for tile in self.current_state_array:
            if tile != self.goal_state_array[index]:
                misplaced_tiles_count += 1
            index += 1
        # Subtracting 1 for count 'b' in misplaced tiles
        misplaced_tiles_count -= 1
        return misplaced_tiles_count

    def no_of_misplaced_tiles(self):
        misplaced_tiles_count = 0

        index = 0
        for tile in self.current_state_array:
            if tile != self.goal_state_array[index]:
                misplaced_tiles_count += 1
            index += 1
        return misplaced_tiles_count
