import math
from math import sqrt

import numpy as np
from sklearn.model_selection import train_test_split

input_data = np.loadtxt('/Test_Data/spambase.data', delimiter=',', dtype=float)
samples, target = input_data[:, :-1], input_data[:, -1]

# Splitting the dataset into training and test data
train_input, test_input, train_target, test_target = train_test_split(samples, target, test_size=0.50, random_state=0)

# Computing Prior Probability of each class in training data
class_one_occurences = np.count_nonzero(train_target[:] == 1)
prior_prob_class_1 = (class_one_occurences / len(train_target))

class_zero_occurences = np.count_nonzero(train_target[:] == 0)
prior_prob_class_0 = (class_zero_occurences / len(train_target))

# Computing mean and standard deviation for all the features
feature_positive_dict = dict()
feature_negative_dict = dict()

for i in range(train_input.shape[1]):
    feature_spam, feature_not_spam = [], []
    for j in range(len(train_target)):
        if train_target[j] == 1:
            feature_spam.append(train_input[j][i])
        else:
            feature_not_spam.append(train_input[j][i])
    feature_spam_mean = np.mean(feature_spam)
    feature_spam_std = np.std(feature_spam)
    if feature_spam_std == 0:
        feature_spam_std = 0.0001
    feature_not_spam_mean = np.mean(feature_not_spam)
    feature_not_spam_std = np.std(feature_not_spam)
    if feature_not_spam_std == 0:
        feature_not_spam_std = 0.0001
    feature_positive_dict.update({i: [feature_spam_mean, feature_spam_std]})
    feature_negative_dict.update({i: [feature_not_spam_mean, feature_not_spam_std]})

# Using the Naive Bayes on the testing data
pos_test_prob_dict = dict()
neg_test_prob_dict = dict()
for m in range(len(test_input)):
    pos_test_prob_list = []
    neg_test_prob_list = []
    for n in range(test_input.shape[1]):
        x = test_input[m][n]

        # Find the probability of the testing data with respect to positive class
        pos_mean = feature_positive_dict.get(n)[0]
        pos_standard_deviation = feature_positive_dict.get(n)[1]
        pos_first_term = (1 / (sqrt(2 * math.pi) * pos_standard_deviation))
        pos_second_term = math.e ** (-(((x - pos_mean) ** 2) / (2 * (pos_standard_deviation ** 2))))
        if pos_second_term <= 0.00000000000000000000000000000000000000001:
            pos_second_term = 0.00000000000000000000000000000000000000001
        pos_prob_of_test_feature = pos_first_term * pos_second_term
        pos_test_prob_list.append(pos_prob_of_test_feature)

        # Find the probability of the testing data with respect to negative class
        neg_mean = feature_negative_dict.get(n)[0]
        neg_standard_deviation = feature_negative_dict.get(n)[1]
        neg_first_term = (1 / (sqrt(2 * math.pi) * neg_standard_deviation))
        neg_second_term = math.e ** (-(((x - neg_mean) ** 2) / (2 * (neg_standard_deviation ** 2))))
        if neg_second_term <= 0.00000000000000000000000000000000000000001:
            neg_second_term = 0.00000000000000000000000000000000000000001
        neg_prob_of_test_feature = neg_first_term * neg_second_term
        neg_test_prob_list.append(neg_prob_of_test_feature)
    pos_test_prob_dict.update({m: pos_test_prob_list})
    neg_test_prob_dict.update({m: neg_test_prob_list})

# Computing the final positive and negative probability of the testing data
correct_predictions = 0
cm_dimensions = (2, 2)
confusion_matrix = np.zeros(cm_dimensions)
for k in range(len(test_target)):
    actual_class = test_target[k]

    positive_prob = 0
    pos_prob_log_sum = 0
    pos_test_prob_list = pos_test_prob_dict.get(k)
    for i in range(len(pos_test_prob_list)):
        pos_prob_log_sum = pos_prob_log_sum + np.log(pos_test_prob_list[i])
    positive_prob = np.log(prior_prob_class_1) + pos_prob_log_sum

    negative_prob = 0
    neg_prob_log_sum = 0
    neg_test_prob_list = neg_test_prob_dict.get(k)
    for i in range(len(neg_test_prob_list)):
        neg_prob_log_sum = neg_prob_log_sum + np.log(neg_test_prob_list[i])
    negative_prob = np.log(prior_prob_class_0) + neg_prob_log_sum

    # Computing the max of the probabilities and creating confusion matrix
    if positive_prob > negative_prob:
        predicted_class = 1
    else:
        predicted_class = 0

    if predicted_class == actual_class:
        correct_predictions = correct_predictions + 1
        for l in range(0, 2):
            for m in range(0, 2):
                if l == m == actual_class:
                    confusion_matrix[l][m] = confusion_matrix[l][m] + 1
                else:
                    continue
    else:
        for l in range(0, 2):
            for m in range(0, 2):
                if l == actual_class and m == predicted_class:
                    confusion_matrix[l][m] = confusion_matrix[l][m] + 1
                else:
                    continue

print("Confusion matrix:  " + str(confusion_matrix))

# TP = True Positive, TN = True Negative, FP = False Positive, FN = False Negative
TP = confusion_matrix[1, 1]
TN = confusion_matrix[0, 0]
FP = confusion_matrix[0, 1]
FN = confusion_matrix[1, 0]

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("Accuracy : %.2f" % accuracy)
print("Precision : %.2f" % precision)
print("Recall : %.2f" % recall)
