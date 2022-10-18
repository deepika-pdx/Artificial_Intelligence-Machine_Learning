import random

from numpy import mean


def generate_grid():
    # Creating 3*3 grid
    grid = []
    for i in range(3):
        grid.append([])
        for j in range(1, 4):
            grid[i].append("Clean")
    return grid


def select_random_location():
    locations_array = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    return locations_array[random.randint(0, 8)]


def add_dirt_pile(number_of_piles, grid):
    for i in range(number_of_piles):
        random_location = select_random_location()
        grid[random_location[0]][random_location[1]] = "Dirty"


def generate_rule_table():
    rule_table = dict()
    rule_table.update({"0,0,Dirty": "Suck"})
    rule_table.update({"0,1,Dirty": "Suck"})
    rule_table.update({"0,2,Dirty": "Suck"})
    rule_table.update({"1,0,Dirty": "Suck"})
    rule_table.update({"1,1,Dirty": "Suck"})
    rule_table.update({"1,2,Dirty": "Suck"})
    rule_table.update({"2,0,Dirty": "Suck"})
    rule_table.update({"2,1,Dirty": "Suck"})
    rule_table.update({"2,2,Dirty": "Suck"})
    rule_table.update({"1,1,Clean": [0, 1]})
    rule_table.update({"0,1,Clean": [0, 0]})
    rule_table.update({"0,0,Clean": [1, 0]})
    rule_table.update({"1,0,Clean": [2, 0]})
    rule_table.update({"2,0,Clean": [2, 1]})
    rule_table.update({"2,1,Clean": [2, 2]})
    rule_table.update({"2,2,Clean": [1, 2]})
    rule_table.update({"1,2,Clean": [0, 2]})
    rule_table.update({"0,2,Clean": [0, 1]})
    return rule_table


def select_random_action():
    actions = ["Left", "Right", "Up", "Down", "Suck", "NoSuck"]
    return actions[random.randint(0, 5)]


def select_random_movement(action, status, pos):
    i = pos[0]
    j = pos[1]
    temp_pos = [i, j]
    if action == "Left":
        temp_pos[1] = j - 1
    elif action == "Right":
        temp_pos[1] = j + 1
    elif action == "Up":
        temp_pos[0] = i - 1
    elif action == "Down":
        temp_pos[0] = i + 1
    if temp_pos[0] < 0 or temp_pos[0] > 2 or temp_pos[1] < 0 or temp_pos[1] > 2 or (
            action == "Suck" and status == "Clean"):
        temp_action = select_random_action()
        temp_random_pos = select_random_movement(temp_action, status, pos)
        return temp_random_pos
    return temp_pos


def simple_reflex_agent():
    performance_measure_array = []
    rules = generate_rule_table()
    for i in range(100):
        number_of_dirt_piles = 5
        dirt_piles_cleaned = 0
        number_of_steps_completed = 0
        total_steps_allowed = 20

        grid = generate_grid()
        add_dirt_pile(number_of_dirt_piles, grid)
        print("Grid: " + str(grid))
        agent_start_location = select_random_location()
        current_location = agent_start_location
        print("Random start location: " + str(current_location))

        for i in range(total_steps_allowed):
            current_state = str(current_location[0]) + "," + str(current_location[1]) + "," + str(
                grid[current_location[0]][
                    current_location[1]])
            corresponding_action = rules.get(current_state)
            if corresponding_action == "Suck":
                grid[current_location[0]][current_location[1]] = "Clean"
                dirt_piles_cleaned += 1
            else:
                next_location = corresponding_action
                current_location = next_location
            number_of_steps_completed += 1
            if number_of_dirt_piles == dirt_piles_cleaned:
                print("Maximum moves allowed: " + str(total_steps_allowed))
                print("Number of moves completed: " + str(number_of_steps_completed))
                steps_ratio = total_steps_allowed / number_of_steps_completed
                performance_measure = steps_ratio * dirt_piles_cleaned
                print("Performance Measure: " + str(performance_measure))
                performance_measure_array.append(performance_measure)
                break
            elif number_of_steps_completed == total_steps_allowed:
                performance_measure = 1 * dirt_piles_cleaned
                performance_measure_array.append(performance_measure)

    print(performance_measure_array)
    average_performance_measure = mean(performance_measure_array)
    print(average_performance_measure)


def randomized_agent():
    performance_measure_array = []
    for i in range(100):
        number_of_dirt_piles = 5
        dirt_piles_cleaned = 0
        number_of_steps_completed = 0
        total_steps_allowed = 20

        grid = generate_grid()
        add_dirt_pile(number_of_dirt_piles, grid)
        print("Grid: " + str(grid))
        agent_start_location = select_random_location()
        current_location = agent_start_location
        print("Random start location: " + str(current_location))

        for i in range(total_steps_allowed):
            status = str(grid[current_location[0]][current_location[1]])
            random_action = select_random_action()
            if random_action == "Suck" and status == "Dirty":
                grid[current_location[0]][current_location[1]] = "Clean"
                dirt_piles_cleaned += 1
            else:
                next_location = select_random_movement(random_action, status, current_location)
                current_location = next_location
            number_of_steps_completed += 1
            if number_of_dirt_piles == dirt_piles_cleaned:
                print("Maximum moves allowed: " + str(total_steps_allowed))
                print("Number of moves completed: " + str(number_of_steps_completed))
                print("Number of dirt piles cleaned: " + str(dirt_piles_cleaned))
                steps_ratio = total_steps_allowed / number_of_steps_completed
                performance_measure = steps_ratio * dirt_piles_cleaned
                print("Performance Measure: " + str(performance_measure))
                performance_measure_array.append(performance_measure)
                break
            elif number_of_steps_completed == total_steps_allowed:
                print("Maximum moves allowed: " + str(total_steps_allowed))
                print("Number of moves completed: " + str(number_of_steps_completed))
                print("Number of dirt piles cleaned: " + str(dirt_piles_cleaned))
                performance_measure = 1 * dirt_piles_cleaned
                print("Performance Measure: " + str(performance_measure))
                performance_measure_array.append(performance_measure)

    print(performance_measure_array)
    average_performance_measure = mean(performance_measure_array)
    print(average_performance_measure)


randomized_agent()
# simple_reflex_agent()
