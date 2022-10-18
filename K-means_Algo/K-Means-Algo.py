import numpy as np

# Importing the dataset from csv to a 2D array
from matplotlib import pyplot as plt

input_data = np.loadtxt('K-means_Dataset/kmeansData.csv', dtype=float)

# Iterating for different values of K
K = 5
r = 10
for i in range(2, K, 1):
    centroid_list = []
    random_values = np.random.randint(0, 1499, i)
    # Initializing the first K centroids randomly
    for j in random_values:
        centroid_list.append(input_data[j])
    centroid_list = np.stack(centroid_list)
    mse_list = []
    centroid_updated_over_runs = []
    # Running the algorithm r times
    cluster_centroids = []
    for k in range(r):
        c_dimensions = (2, 2)
        cluster_data_for_all_centroids = np.zeros(c_dimensions)
        centroid_data_dict = ()
        for data in input_data:
            euclidean_distance = []
            # Assignment Step
            for centroid in centroid_list:
                distance = np.sqrt(np.sum((data - centroid) ** 2))
                euclidean_distance.append(distance)
            min_index = np.argmin(euclidean_distance)
            if len(cluster_centroids) == 0:
                data_centroid = [centroid_list[min_index][0], centroid_list[min_index][1]]
                cluster_centroids.append(data_centroid)
                cluster_data = [data[0], data[1]]
                cluster_data_for_all_centroids = np.vstack(cluster_data_for_all_centroids, cluster_data)
                centroid_data_dict.update({cluster_centroids.index(data_centroid): cluster_data_for_all_centroids})
            else:
                data_centroid = [centroid_list[min_index][0], centroid_list[min_index][1]]
                if cluster_centroids.count(data_centroid) > 0:
                    cluster_data_temp = [data[0], data[1]]
                    centroid_index = cluster_centroids.index(data_centroid)
                    cluster_data_for_all_centroids = centroid_data_dict[centroid_index]
                    cluster_data_for_all_centroids = np.vstack((cluster_data_for_all_centroids, cluster_data_temp))
                else:
                    cluster_centroids.append(data_centroid)
                    cluster_data_temp = [data[0], data[1]]
                    centroid_index = cluster_centroids.index(data_centroid)
                    cluster_data_for_all_centroids = centroid_data_dict[centroid_index]
                    cluster_data_for_all_centroids = np.vstack((cluster_data_for_all_centroids, cluster_data_temp))

        # Maximization Step
        mse_all_clusters = []
        cluster_tracker = 0
        for cData in cluster_data_for_all_centroids:
            x_mean = np.mean(cData[:, 0])
            y_mean = np.mean(cData[:, 1])
            new_centroid = [x_mean, y_mean]

            # Calculating the MSE
            cluster_centroid_old = cluster_centroids[cluster_tracker]
            cluster_count = len(cData)
            distance_sum = 0
            for datapoint in cData:
                cent_data_dist = np.sqrt(np.sum((datapoint - cluster_centroid_old) ** 2))
                distance_sum = distance_sum + (cent_data_dist ** 2)
            mse = distance_sum / cluster_count
            mse_all_clusters.append(mse)
            cluster_centroids[cluster_tracker] = new_centroid
            cluster_tracker = cluster_tracker + 1
        centroid_list = cluster_centroids

    # Visualizing the data after r runs of k-means for some K

    counter = 0
    for centroid in centroid_list:
        centroid_data = cluster_data_for_all_centroids[counter]
        plt.scatter(centroid_data[:, 0], centroid_data[:, 1], label=centroid)
        counter = counter + 1
    plt.legend()
    plt.show()
