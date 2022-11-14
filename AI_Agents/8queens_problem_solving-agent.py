import random
from math import floor

import matplotlib.pyplot as plt
from numpy import mean
from numpy.random import choice


def count_non_attacking_queens(queens_config):
    count_of_attacking_queens = 0
    while len(queens_config) > 1:
        each_queen = queens_config[0]
        for q in range(1, len(queens_config)):
            # Checking if two queens are in the same row
            if each_queen[0] == queens_config[q][0]:
                count_of_attacking_queens += 1
            # Checking if two queens are in the same column
            elif each_queen[1] == queens_config[q][1]:
                count_of_attacking_queens += 1
            # Checking if two queens are on the same diagonal 1
            elif (each_queen[0] + each_queen[1]) == (queens_config[q][0] + queens_config[q][1]):
                count_of_attacking_queens += 1
            # Checking if two queens are on the same diagonal 2
            elif (each_queen[0] - each_queen[1]) == (queens_config[q][0] - queens_config[q][1]):
                count_of_attacking_queens += 1
        queens_config.pop(0)
    count_of_non_attacking_queens = 28 - count_of_attacking_queens
    return count_of_non_attacking_queens


class EightQueensProblemSolvingAgent:
    def __init__(self):
        self.population = []
        self.fitness_function = []
        self.population_norm_fitness_fn_dict = {}

    def generate_8_queens_initial_population(self, count):
        for i in range(count):
            individual = [random.randint(0, 7) for j in range(0, 8)]
            self.population.append(individual)

    def determine_fitness_function_of_initial_population(self):
        for state in self.population:
            queen_configuration = []
            col_number = 0
            for queen in state:
                queen_configuration.append([queen, col_number])
                col_number += 1

            fitness_value = count_non_attacking_queens(queen_configuration)
            self.fitness_function.append(fitness_value)

    def normalise_fitness_function(self):
        population_index = 0
        pop_norm_ff_dict = {}
        for fitness_fn in self.fitness_function:
            normalised_fitness_fn = fitness_fn / sum(self.fitness_function)
            pop_norm_ff_dict.update({population_index: normalised_fitness_fn})
            population_index += 1
        self.population_norm_fitness_fn_dict = pop_norm_ff_dict

    def perform_crossover(self):
        next_gen_population = []
        next_gen_fitness_function = []

        parent_list = list(self.population_norm_fitness_fn_dict.keys())
        norm_fitness_list = list(self.population_norm_fitness_fn_dict.values())

        no_of_pairs = floor(len(parent_list) / 2)
        for s in range(no_of_pairs):
            selected_parents_indices = choice(parent_list, 2, p=norm_fitness_list)
            while selected_parents_indices[1] == selected_parents_indices[0]:
                selected_parents_indices[1] = random.choices(parent_list, weights=norm_fitness_list, k=1)[0]

            parent_1 = self.population[selected_parents_indices[0]]
            parent_2 = self.population[selected_parents_indices[1]]

            crossover_point = random.randint(1, 5)
            child_1 = []
            child_2 = []
            child_array = []

            # Perform crossover
            for k in range(len(parent_1)):
                if k <= crossover_point:
                    child_1.append(parent_1[k])
                    child_2.append(parent_2[k])
                else:
                    child_1.append(parent_2[k])
                    child_2.append(parent_1[k])

            # Perform mutation by deciding randomly when to mutate such that the mutation rate is maintained
            should_mutate = choice([True, False], 1, p=[0.10, 0.90])

            if should_mutate:
                mutation_index_1 = random.randint(0, 7)
                child_1[mutation_index_1] = mutation_index_1

                mutation_index_2 = random.randint(0, 7)
                child_2[mutation_index_2] = mutation_index_2

            child_array.append(child_1)
            child_array.append(child_2)
            next_gen_population.append(child_1)
            next_gen_population.append(child_2)

            # Calculate fitness function of the children
            child_fitness_array = []

            for child in child_array:
                child_configuration = []
                col_number = 0
                for child_queen in child:
                    child_configuration.append([child_queen, col_number])
                    col_number += 1

                child_fitness_value = count_non_attacking_queens(child_configuration)
                child_fitness_array.append(child_fitness_value)

            next_gen_fitness_function.append(child_fitness_array[0])
            next_gen_fitness_function.append(child_fitness_array[1])

        self.population = next_gen_population
        self.fitness_function = next_gen_fitness_function
        self.normalise_fitness_function()


if __name__ == '__main__':
    no_of_iterations = 1000
    eight_queens = EightQueensProblemSolvingAgent()

    # Generate initial population i.e. random 8 queens state such that each queen is in one column
    population_count = 1000
    eight_queens.generate_8_queens_initial_population(population_count)
    print("Initial Population: " + str(eight_queens.population))

    # Determine the fitness function of each individual in the population
    # i.e. determine the number of non-attacking queens for each state in the initial population
    eight_queens.determine_fitness_function_of_initial_population()
    print("Fitness function of initial population: " + str(eight_queens.fitness_function))
    print("Mean of Fitness function of initial population: " + str(mean(eight_queens.fitness_function)))

    # Normalise the fitness function of each individual in the population
    eight_queens.normalise_fitness_function()
    x_axis = []
    y_axis = []
    for iteration in range(no_of_iterations):
        # Select the pair of individuals with the highest normalised fitness function value and perform crossover
        # and add the children back to the population
        eight_queens.perform_crossover()

        x_axis.append(iteration)
        y_axis.append(mean(eight_queens.fitness_function))
        print("Mean of Fitness function of population after " + str(iteration) + " iterations: " + str(mean(
            eight_queens.fitness_function)))

        if iteration == (no_of_iterations - 1):
            print("Final states of population after " + str(iteration) + " iterations: " + str(
                eight_queens.population))
            print("Fitness function of population after " + str(iteration) + " iterations: " + str(
                eight_queens.fitness_function))
            print("Mean of Fitness function of population after " + str(iteration) + " iterations: " + str(mean(
                eight_queens.fitness_function)))
    plt.xlabel("Number of iterations")
    plt.ylabel("Average fitness function")
    plt.title("Average fitness function vs Number of iterations (MutationPct = 0.1")
    plt.plot(x_axis, y_axis)
    plt.show()
