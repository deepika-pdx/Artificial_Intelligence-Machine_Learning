def check_parity(puzzle_array):
    parity_count = 0
    for tile in puzzle_array:
        if tile == 'b':
            continue
        index_of_tile = puzzle_array.index(tile)
        for j in range(index_of_tile):
            if puzzle_array[j] == 'b':
                continue
            if puzzle_array[j] > tile:
                parity_count += 1

    print(parity_count)
    parity_value = "even_parity" if parity_count % 2 == 0 else "odd_parity"
    return parity_value


class PuzzleParityCheck:

    def __init__(self, input_puzzle_1, input_puzzle_2):
        self.input_puzzle_1 = input_puzzle_1
        self.input_puzzle_2 = input_puzzle_2

    def compare_puzzle_parity(self):
        puzzle_1_array = []
        for puzzle_row in self.input_puzzle_1:
            for tile in puzzle_row:
                puzzle_1_array.append(tile)

        puzzle_2_array = []
        for puzzle_row in self.input_puzzle_2:
            for tile in puzzle_row:
                puzzle_2_array.append(tile)

        puzzle_1_parity = check_parity(puzzle_1_array)
        puzzle_2_parity = check_parity(puzzle_2_array)

        is_state_reachable = True if puzzle_1_parity == puzzle_2_parity else False
        return is_state_reachable
