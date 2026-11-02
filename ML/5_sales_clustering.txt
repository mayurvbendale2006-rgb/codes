
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Dataset Shape:", df.shape)

# Select numerical features
X = df[["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]]

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Apply K-Means Clustering
# Change this value if the elbow graph indicates a different number.
k = 3

kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df["KMeans_Cluster"] = kmeans.fit_predict(X_scaled)

print("\nK-Means Cluster Counts:")
print(df["KMeans_Cluster"].value_counts().sort_index())

# Visualize K-Means Clusters
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 2],
    c=df["KMeans_Cluster"], cmap="viridis"
)
plt.title("K-Means Clustering")
plt.xlabel("Quantity Ordered (Scaled)")
plt.ylabel("Sales (Scaled)")
plt.show()

# Apply Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=k, linkage="ward")
df["Hierarchical_Cluster"] = hc.fit_predict(X_scaled)

print("\nHierarchical Cluster Counts:")
print(df["Hierarchical_Cluster"].value_counts().sort_index())

# Visualize Hierarchical Clusters
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 2],
    c=df["Hierarchical_Cluster"], cmap="rainbow"
)
plt.title("Hierarchical Clustering")
plt.xlabel("Quantity Ordered (Scaled)")
plt.ylabel("Sales (Scaled)")
plt.show()
