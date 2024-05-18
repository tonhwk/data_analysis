import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Visualize the original dataset
plt.figure(figsize=(8, 6))
for i in range(len(iris.feature_names)):
    plt.scatter(df.iloc[:, i], iris.target, label=iris.feature_names[i])
plt.xlabel('Features')
plt.ylabel('Species')
plt.title('Original Dataset (Iris)')
plt.legend()
plt.show()

# Perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df)

# Create a DataFrame for the principal components
pc_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Visualize the transformed dataset
plt.figure(figsize=(8, 6))
plt.scatter(pc_df['PC1'], pc_df['PC2'], c=iris.target, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Transformed Dataset (PCA)')
plt.colorbar(label='Species')
plt.show()
