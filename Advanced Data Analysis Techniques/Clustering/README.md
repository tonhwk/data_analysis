# Mall Customers Dataset for Clustering Analysis

## Dataset Description

The `mall_customers.csv` dataset contains information about customers of a shopping mall. It is used to understand customer behaviors and segment them into different groups based on their annual income and spending scores. This dataset is particularly useful for practicing clustering algorithms and exploring customer segmentation.

### Columns

1. **CustomerID**: 
   - **Description**: A unique identifier assigned to each customer.
   - **Type**: Integer

2. **Gender**: 
   - **Description**: The gender of the customer.
   - **Type**: Categorical (Male/Female)

3. **Age**: 
   - **Description**: The age of the customer.
   - **Type**: Integer

4. **Annual_Income_(k$)**: 
   - **Description**: The annual income of the customer in thousands of dollars.
   - **Type**: Integer

5. **Spending_Score**: 
   - **Description**: A score assigned to the customer based on their spending behavior and purchasing patterns. 
   - **Type**: Integer (Range: 1 to 100)

## Goal

The primary goal of using this dataset is to perform customer segmentation using advanced clustering algorithms. By clustering the customers based on their annual income and spending score, we can identify distinct groups of customers with similar behaviors. This information can be valuable for targeted marketing, personalized recommendations, and improving customer satisfaction.

## Clustering Algorithms

In this project, we will explore and apply various clustering algorithms including:

1. **K-Means Clustering**
   - A simple and widely used clustering algorithm that partitions the dataset into K clusters based on the features.

2. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
   - An algorithm that groups together points that are closely packed and marks points in low-density regions as outliers.

3. **Agglomerative Hierarchical Clustering**
   - A bottom-up clustering method where each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.

4. **Gaussian Mixture Models (GMM)**
   - A probabilistic model that assumes the data is generated from a mixture of several Gaussian distributions with unknown parameters.

5. **Mean Shift Clustering**
   - A non-parametric clustering technique that aims to find blobs in a smooth density of samples.

## How to Use

1. **Data Preprocessing**
   - Convert categorical features (e.g., Gender) to numerical values.
   - Normalize the numerical features (e.g., Age, Annual Income, Spending Score) to ensure they are on a similar scale.

2. **Exploratory Data Analysis (EDA)**
   - Visualize the distributions of Age, Annual Income, and Spending Score.
   - Analyze correlations between features.

3. **Clustering Analysis**
   - Apply various clustering algorithms to the dataset.
   - Determine the optimal number of clusters using methods like the elbow method for K-means or silhouette scores for other algorithms.
   - Visualize the resulting clusters to interpret the segments.

## Example Code

Here’s a snippet to get you started with K-Means clustering:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('mall_customers.csv')

# Data preprocessing
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
features = ['Age', 'Annual_Income_(k$)', 'Spending_Score']
X = data[features]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot the clusters
plt.scatter(data['Annual_Income_(k$)'], data['Spending_Score'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.title('Customer Segments')
plt.show()
