import numpy as np
from matplotlib import pyplot as plt


class K_Means_Algo:

    def __init__(self, k, r):
        self.k = k
        self.r = r

    def euclidean_distance(self, datapoint, centroid):
        return np.sqrt(np.sum((datapoint - centroid) ** 2))

    def fit(self, data):
        # Initializing the first K centroids as first K values of the input data
        self.centroids = {}
        self.mse_list = []
        self.avg_mse = 0
        for i in range(self.k):
            self.centroids[i] = data[i]

        # Initializing K clusters with empty array
        for i in range(self.r):
            self.clusters = {}
            for j in range(self.k):
                self.clusters[j] = []

            # Assigning input data points to the nearest centroid
            for point in data:
                distances = []
                for index in self.centroids:
                    distances.append(self.euclidean_distance(point, self.centroids[index]))
                cluster_index = distances.index(min(distances))
                self.clusters[cluster_index].append(point)

            # Updating the values of the centroid for each cluster
            previous = dict(self.centroids)
            for cluster_index in self.clusters:
                self.centroids[cluster_index] = np.mean(self.clusters[cluster_index], axis=0)

            # Computing the MSE and Average MSE
            for cluster_index in self.clusters:
                cluster_datapoints = self.clusters[cluster_index]
                cluster_count = len(cluster_datapoints)
                cluster_centroid = previous[cluster_index]
                distance_sum = 0
                for datapoint in cluster_datapoints:
                    cent_data_dist = np.sqrt(np.sum((datapoint - cluster_centroid) ** 2))
                    distance_sum = distance_sum + (cent_data_dist ** 2)
                mse = distance_sum / cluster_count
                self.mse_list.append(mse)
        self.avg_mse = np.mean(self.mse_list)


K = 2
r = 10
input_data = np.loadtxt('K-means_Dataset/kmeansData.csv', dtype=float)
k_means_instance = K_Means_Algo(K, r)
k_means_instance.fit(input_data)
print("Avg_Mean: " + str(k_means_instance.avg_mse))

colors = 10 * ['red', 'green', 'blue', 'yellow', 'lightcoral', 'darkorange', 'violet', 'skyblue', 'olive', 'black']
for cluster_index in k_means_instance.clusters:
    color = colors[cluster_index]
    for features in k_means_instance.clusters[cluster_index]:
        plt.scatter(features[0], features[1], color=color, s=30)
plt.show()
