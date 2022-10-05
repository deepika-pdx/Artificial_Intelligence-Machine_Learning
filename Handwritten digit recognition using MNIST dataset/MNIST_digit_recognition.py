import csv
import json
import sys
import time

import numpy as np
from xlwt import Workbook

# Workbook is created
wb = Workbook()
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
start_time = time.time()

# Reading the MNIST Data
training_data_csv = open('G:/USA/Masters/Graduate/CS 545/HW/MNIST_Dataset/mnist_train.csv')
testing_data_csv = open('G:/USA/Masters/Graduate/CS 545/HW/MNIST_Dataset/mnist_test.csv')
training_data_reader = csv.reader(training_data_csv)
testing_data_reader = csv.reader(testing_data_csv)

# File to write output
file_path = 'G:/USA/Masters/Graduate/CS 545/HW/MNIST_Dataset/output_11.txt'
sys.stdout = open(file_path, "w")

# Extract training data from csv into matrix
training_header = []
training_header = next(training_data_reader)
training_data_set = []
training_data_set = [[json.loads(item) for item in training_row] for training_row in training_data_reader]

# Extract testing data from csv into matrix
testing_header = []
testing_header = next(testing_data_reader)
testing_data_set = []
testing_data_set = [[json.loads(item) for item in testing_row] for testing_row in testing_data_reader]

# Extracting the targets from training and testing data
training_targets = np.transpose(training_data_set)[0]
testing_targets = np.transpose(testing_data_set)[0]

# Normalising the training data
normalized_training_data = []
for training_data in training_data_set:
    training_data[0] = 1
    normalized_training_data.append(np.divide(training_data, 255))

# Normalising the testing data
normalized_testing_data = []
for testing_data in testing_data_set:
    testing_data[0] = 1
    normalized_testing_data.append(np.divide(testing_data, 255))

# Generating random initial weights
initial_weights = np.random.uniform(-0.05, 0.05, size=(10, 785))

# Passing the values to the perceptron
eta = 0.1
epoch = 70
for e in range(epoch):

    training_index = 0

    for data in normalized_training_data:
        wx = np.dot(data, np.transpose(initial_weights))
        y = []
        for op in wx:
            if op > 0:
                y.append(1)
            else:
                y.append(0)

        # Getting the corresponding target
        target = training_targets[training_index]
        t = []
        for i in range(0, 10):
            if i == target:
                t.append(1)
            else:
                t.append(0)
        # Checking if y = t
        if np.array_equal(y, t):
            training_index = training_index + 1
        else:
            for i in range(0, 10):
                diff = y[i] - t[i]
                initial_weights[i] = initial_weights[i] - (eta * diff * data)
            training_index = training_index + 1

    print('-------------------------------Training Results------------------------------------------')
    training_index = 0
    correct_prediction = 0
    wrong_prediction = 0
    for data in normalized_training_data:
        wx = np.dot(data, np.transpose(initial_weights))
        y = np.argmax(wx)

        # Getting the corresponding target
        t = training_targets[training_index]

        # Checking if y = t
        if y == t:
            correct_prediction = correct_prediction + 1
            training_index = training_index + 1
        else:
            wrong_prediction = wrong_prediction + 1
            training_index = training_index + 1
    training_accuracy = (correct_prediction / 60000) * 100
    sheet1.write(e, 0, training_accuracy)
    print("Accuracy of training after epoch " + str(e) + " : " + str(training_accuracy))

    print('-------------------------------Testing Results------------------------------------------')

    testing_index = 0
    correct_prediction = 0
    wrong_prediction = 0
    if e == 69:
        final_correct_targets = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_0 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_1 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_2 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_3 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_4 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_5 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_6 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_7 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_8 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
        final_incorrect_targets_9 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}
    for data in normalized_testing_data:
        wx = np.dot(data, np.transpose(initial_weights))
        y = np.argmax(wx)

        # Getting the corresponding target
        t = testing_targets[testing_index]

        # Checking if y = t
        if y == t:
            if e == 69:
                for correct in final_correct_targets:
                    if int(correct) == t:
                        final_correct_targets[correct] += 1
            correct_prediction = correct_prediction + 1
            testing_index = testing_index + 1
        else:
            if e == 69:
                if t == 0:
                    for incorrect in final_incorrect_targets_0:
                        if int(incorrect) == y:
                            final_incorrect_targets_0[y] += 1
                elif t == 1:
                    for incorrect in final_incorrect_targets_1:
                        if int(incorrect) == y:
                            final_incorrect_targets_1[y] += 1
                elif t == 2:
                    for incorrect in final_incorrect_targets_2:
                        if int(incorrect) == y:
                            final_incorrect_targets_2[y] += 1
                elif t == 3:
                    for incorrect in final_incorrect_targets_3:
                        if int(incorrect) == y:
                            final_incorrect_targets_3[y] += 1
                elif t == 4:
                    for incorrect in final_incorrect_targets_4:
                        if int(incorrect) == y:
                            final_incorrect_targets_4[y] += 1
                elif t == 5:
                    for incorrect in final_incorrect_targets_5:
                        if int(incorrect) == y:
                            final_incorrect_targets_5[y] += 1
                elif t == 6:
                    for incorrect in final_incorrect_targets_6:
                        if int(incorrect) == y:
                            final_incorrect_targets_6[y] += 1
                elif t == 7:
                    for incorrect in final_incorrect_targets_7:
                        if int(incorrect) == y:
                            final_incorrect_targets_7[y] += 1
                elif t == 8:
                    for incorrect in final_incorrect_targets_8:
                        if int(incorrect) == y:
                            final_incorrect_targets_8[y] += 1
                elif t == 9:
                    for incorrect in final_incorrect_targets_9:
                        if int(incorrect) == y:
                            final_incorrect_targets_9[y] += 1
            wrong_prediction = wrong_prediction + 1
            testing_index = testing_index + 1
    testing_accuracy = (correct_prediction / 10000) * 100
    sheet1.write(e, 1, testing_accuracy)

    if e == 69:
        count = 0
        for correct in final_correct_targets:
            print("Number of correct " + str(count) + " are " + str(final_correct_targets[correct]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_0:
            print("Number of incorrect " + str(count) + "in 0 are " + str(final_incorrect_targets_0[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_1:
            print("Number of incorrect " + str(count) + "in 1 are " + str(final_incorrect_targets_1[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_2:
            print("Number of incorrect " + str(count) + "in 2 are " + str(final_incorrect_targets_2[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_3:
            print("Number of incorrect " + str(count) + "in 3 are " + str(final_incorrect_targets_3[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_4:
            print("Number of incorrect " + str(count) + "in 4 are " + str(final_incorrect_targets_4[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_5:
            print("Number of incorrect " + str(count) + "in 5 are " + str(final_incorrect_targets_5[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_6:
            print("Number of incorrect " + str(count) + "in 6 are " + str(final_incorrect_targets_6[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_7:
            print("Number of incorrect " + str(count) + "in 7 are " + str(final_incorrect_targets_7[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_8:
            print("Number of incorrect " + str(count) + "in 8 are " + str(final_incorrect_targets_8[incorrect]))
            count = count + 1

        count = 0
        for incorrect in final_incorrect_targets_9:
            print("Number of incorrect " + str(count) + "in 9 are " + str(final_incorrect_targets_9[incorrect]))
            count = count + 1

    print("Accuracy of testing after epoch " + str(e) + " : " + str(testing_accuracy))

print("--- %s seconds ---" % (time.time() - start_time))

wb.save('xlwt example.xls')
