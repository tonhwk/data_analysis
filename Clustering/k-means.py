import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = {
    'Feature1': [1, 2, 2, 3, 3, 4, 4, 5, 6, 6],
    'Feature2': [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
}

df = pd.DataFrame(data)

# Visualize the dataset
plt.scatter(df['Feature1'], df['Feature2'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Original Dataset')
plt.show()

# Perform K-means clustering
kmeans = KMeans(n_clusters=2)
kmeans.fit(df)

# Get cluster centers and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Visualize the clusters
plt.scatter(df['Feature1'], df['Feature2'], c=labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', color='red', s=200, label='Cluster Centers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering')
plt.legend()
plt.show()
