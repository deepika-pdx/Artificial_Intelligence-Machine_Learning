import math
import random
import matplotlib.pyplot as plt
from numpy import mean
from numpy.random import choice
import numpy as np


class RobotReinforcementLearningAgent:
    def __init__(self):
        self.grid = []
        self.Q_matrix = []
        self.actions = ["Move_North", "Move_South", "Move_East", "Move_West", "Pick_up_can"]
        self.epsilon = 0.1
        self.no_of_episodes = 5000
        self.no_of_steps_in_each_episode = 200
        self.rewards_per_episode = []
        self.eta = 0.2
        self.gamma = 0.9
        self.training_episode_value = []
        self.training_reward_value = []

    def generate_initial_grid(self):
        for i in range(10):
            each_row_in_grid = [1 if choice([True, False], 1, p=[0.5, 0.5]) == True else 0 for j in range(10)]
            self.grid.append(each_row_in_grid)

    def generate_Q_matrix(self):
        first_row = ["Q(s,a)", "Move_North", "Move_South", "Move_East", "Move_West", "Pick_up_can"]
        self.Q_matrix.append(first_row)
        for i in range(10):
            for j in range(10):
                each_row = [(i, j)]
                each_row.append([0 for k in range(5)])
                self.Q_matrix.append(each_row)

    def get_sensor_info(self, robby_x_pos, robby_y_pos):
        sensor_info = []
        # Determine current position state using sensor
        if self.grid[robby_x_pos][robby_y_pos] == 1:
            sensor_info.append("Can")
        else:
            sensor_info.append("Empty")

        # Determine north state wrt current position using sensor
        if robby_x_pos - 1 < 0:
            sensor_info.append("Wall")
        elif self.grid[robby_x_pos - 1][robby_y_pos] == 1:
            sensor_info.append("Can")
        else:
            sensor_info.append("Empty")

        # Determine south state wrt current position using sensor
        if robby_x_pos + 1 > 9:
            sensor_info.append("Wall")
        elif self.grid[robby_x_pos + 1][robby_y_pos] == 1:
            sensor_info.append("Can")
        else:
            sensor_info.append("Empty")

        # Determine east state wrt current position using sensor
        if robby_y_pos + 1 > 9:
            sensor_info.append("Wall")
        elif self.grid[robby_x_pos][robby_y_pos + 1] == 1:
            sensor_info.append("Can")
        else:
            sensor_info.append("Empty")

        # Determine west state wrt current position using sensor
        if robby_y_pos - 1 < 0:
            sensor_info.append("Wall")
        elif self.grid[robby_x_pos][robby_y_pos - 1] == 1:
            sensor_info.append("Can")
        else:
            sensor_info.append("Empty")

        return sensor_info

    def select_an_action(self, x_pos, y_pos):

        # if np.random.random() < self.epsilon:
        #     selected_action_index = np.argmax(self.Q_matrix[((x_pos * 10) + y_pos + 1)][1])
        # else:
        #     selected_action_index = np.random.randint(0, 5)
        #
        # action = self.actions[selected_action_index]

        qsa_row = self.Q_matrix[((x_pos * 10) + y_pos + 1)][1]
        max_qsa = max(qsa_row)
        q_based_action = self.actions[qsa_row.index(max_qsa)]
        random_action = self.actions[random.randint(0, 4)]

        action = choice([q_based_action, random_action], 1, p=[(1 - self.epsilon), self.epsilon])
        return action


if __name__ == '__main__':
    robby_robot = RobotReinforcementLearningAgent()
    robby_robot.generate_Q_matrix()

    # ---------------------------------------------------------Training----------------------------------------------------------------------
    # for each episode
    for episode in range(robby_robot.no_of_episodes):
        print("Episode number: " + str(episode))
        robby_robot.grid = []
        robby_robot.generate_initial_grid()
        print("Print initial grid: " + str(robby_robot.grid))
        starting_x = random.randint(0, 9)
        starting_y = random.randint(0, 9)
        rewards_in_this_episode = 0
        no_of_cans_collected = 0

        robby_current_x = starting_x;
        robby_current_y = starting_y

        # # Reducing the value of epsilon after every 50 episodes
        if robby_robot.epsilon == 0.01000000000000001:
            robby_robot.epsilon = 0.00000000000000001
        if (robby_robot.epsilon != 0 and robby_robot.epsilon != 0.00000000000000001 and
                episode != 0 and episode % 50 == 0):
            robby_robot.epsilon -= 0.01

        for time_step in range(robby_robot.no_of_steps_in_each_episode):
            reward = 0
            # Choose an action using epsilon-greedy action selection
            selected_action = robby_robot.select_an_action(robby_current_x, robby_current_y)
            robby_sensor_info = robby_robot.get_sensor_info(robby_current_x, robby_current_y)

            robby_next_x = 0
            robby_next_y = 0
            if selected_action == "Pick_up_can":
                if robby_sensor_info[0] == "Can":
                    # Removing the can from the grid
                    robby_robot.grid[robby_current_x][robby_current_y] = 0
                    reward = 10
                    no_of_cans_collected += 1
                else:
                    reward = -1
                robby_next_x = robby_current_x
                robby_next_y = robby_current_y
            elif selected_action == "Move_North":
                if robby_sensor_info[1] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x - 1
                    robby_next_y = robby_current_y
            elif selected_action == "Move_South":
                if robby_sensor_info[2] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x + 1
                    robby_next_y = robby_current_y
            elif selected_action == "Move_East":
                if robby_sensor_info[3] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y + 1
            else:
                if robby_sensor_info[4] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y - 1

            # Getting current state Q(s,a) value from Q-matrix
            q_matrix_current_x = (robby_current_x * 10) + robby_current_y + 1
            q_matrix_current_y = robby_robot.actions.index(selected_action)
            Qsa_row = robby_robot.Q_matrix[q_matrix_current_x][1]
            Qsa_current_value = Qsa_row[q_matrix_current_y]

            # Getting next state max(Q(s,a)) value from Q-matrix
            q_matrix_next_x = (robby_next_x * 10 + robby_next_y) + 1
            Qsa_next_row = robby_robot.Q_matrix[q_matrix_next_x][1]
            Qsa_next_max_value = max(Qsa_next_row)

            # Calculating the updated values of Q(s,a) using Q-Learning algorithm
            Qsa_updated_value = Qsa_current_value + robby_robot.eta * (
                    reward + (robby_robot.gamma * Qsa_next_max_value) - Qsa_current_value)

            # Updating the new Q(s,a) value in original Q-matrix
            robby_robot.Q_matrix[q_matrix_current_x][1][q_matrix_current_y] = Qsa_updated_value

            robby_current_x = robby_next_x
            robby_current_y = robby_next_y
            rewards_in_this_episode += reward

        print("Print grid after episode: " + str(robby_robot.grid))
        print("Rewards in this episode: " + str(rewards_in_this_episode))
        print("Cans collected in this episode: " + str(no_of_cans_collected))
        robby_robot.rewards_per_episode.append(rewards_in_this_episode)
        if episode != 0 and episode % 100 == 0:
            robby_robot.training_episode_value.append(episode)
            robby_robot.training_reward_value.append(rewards_in_this_episode)

    plt.title("Training reward plot (rewards vs episode number)")
    plt.xlabel("Episode number")
    plt.ylabel("Total rewards in the episode")
    plt.plot(robby_robot.training_episode_value, robby_robot.training_reward_value)
    plt.show()

    # ---------------------------------------------------------Testing----------------------------------------------------------------------

    robby_robot.rewards_per_episode = []
    robby_robot.training_episode_value = []
    robby_robot.training_reward_value = []
    # for each episode
    for episode in range(robby_robot.no_of_episodes):
        print("Episode number: " + str(episode))
        robby_robot.grid = []
        robby_robot.generate_initial_grid()
        starting_x = random.randint(0, 9)
        starting_y = random.randint(0, 9)
        rewards_in_this_episode = 0
        no_of_cans_collected = 0

        robby_current_x = starting_x;
        robby_current_y = starting_y

        robby_robot.epsilon = 0.1

        for time_step in range(robby_robot.no_of_steps_in_each_episode):
            reward = 0
            # Choose an action using epsilon-greedy action selection
            selected_action = robby_robot.select_an_action(robby_current_x, robby_current_y)
            robby_sensor_info = robby_robot.get_sensor_info(robby_current_x, robby_current_y)

            robby_next_x = 0
            robby_next_y = 0
            if selected_action == "Pick_up_can":
                if robby_sensor_info[0] == "Can":
                    # Removing the can from the grid
                    robby_robot.grid[robby_current_x][robby_current_y] = 0
                    reward = 10
                    no_of_cans_collected += 1
                else:
                    reward = -1
                robby_next_x = robby_current_x
                robby_next_y = robby_current_y
            elif selected_action == "Move_North":
                if robby_sensor_info[1] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x - 1
                    robby_next_y = robby_current_y
            elif selected_action == "Move_South":
                if robby_sensor_info[2] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x + 1
                    robby_next_y = robby_current_y
            elif selected_action == "Move_East":
                if robby_sensor_info[3] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y + 1
            else:
                if robby_sensor_info[4] == "Wall":
                    reward = -5
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y
                else:
                    robby_next_x = robby_current_x
                    robby_next_y = robby_current_y - 1

            robby_current_x = robby_next_x
            robby_current_y = robby_next_y
            rewards_in_this_episode += reward

        print("Rewards in this episode: " + str(rewards_in_this_episode))
        print("Cans collected in this episode: " + str(no_of_cans_collected))
        robby_robot.rewards_per_episode.append(rewards_in_this_episode)
        if episode != 0 and episode % 100 == 0:
            robby_robot.training_episode_value.append(episode)
            robby_robot.training_reward_value.append(rewards_in_this_episode)

    test_average = mean(robby_robot.rewards_per_episode)
    print("Test average: " + str(test_average))

    square_summation = 0
    for value in robby_robot.rewards_per_episode:
        square_summation += (value - test_average) ** 2
    test_standard_deviation = math.sqrt(square_summation / robby_robot.no_of_episodes)
    print("Test Standard Deviation: " + str(test_standard_deviation))
