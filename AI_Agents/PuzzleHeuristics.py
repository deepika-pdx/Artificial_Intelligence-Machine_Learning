class PuzzleHeuristics:
    def __init__(self, current_state, goal_state):
        self.current_state = current_state
        self.goal_state = goal_state
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
        if misplaced_tiles_count != 0:
            misplaced_tiles_count -= 1
        return misplaced_tiles_count

    def sum_of_tile_manhatten_distances(self):
        sum_distance = 0

        state_length = len(self.current_state)
        for i in range(state_length):
            for j in range(state_length):
                tile = self.current_state[i][j]
                for m in range(state_length):
                    for n in range(state_length):
                        if self.goal_state[m][n] == tile:
                            m_distance = abs(i - m) + abs(j - n)
                            sum_distance = sum_distance + m_distance
                        else:
                            continue
        return sum_distance
