import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

file_path = r"C:\Users\Rudra\Desktop\CENSUS_PROJECT_WOMEN\White_Fertility\4_final_data\data_without_year123.csv"
data = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(data.head())

data_numeric = data.select_dtypes(include=["float64", "int64"])

print("\nMissing values in the dataset:")
print(data_numeric.isnull().sum())
data_numeric = data_numeric.dropna()


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric)


pca = PCA()
pca.fit(data_scaled)


data_pca = pca.transform(data_scaled)

explained_variance_ratio = pca.explained_variance_ratio_

cumulative_explained_variance = explained_variance_ratio.cumsum()

plt.figure(figsize=(10, 6))
plt.plot(
    range(1, len(explained_variance_ratio) + 1),
    cumulative_explained_variance,
    marker="o",
)
plt.title("Cumulative Explained Variance by Principal Components")
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative Explained Variance")
plt.grid(True)
plt.show()

target_variance = 0.92
num_components = (
    cumulative_explained_variance <= target_variance
).sum() + 1  # +1 to include the component that exceeds the threshold

print(
    f"\nNumber of components to explain {target_variance*100}% variance: {num_components}"
)

pca = PCA(n_components=num_components)
data_pca_reduced = pca.fit_transform(data_scaled)

print(
    f"\nShape of the PCA-transformed data with {num_components} components: {data_pca_reduced.shape}"
)
# pd.DataFrame(
# data_pca_reduced, columns=[f"PC{i+1}" for i in range(num_components)]
# ).to_csv("pca_analysis.csv", index=False)
