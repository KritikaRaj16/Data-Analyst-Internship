import pandas as pd

# Load the sales dataset
data = pd.read_csv("sales.csv")

# Display the first 5 rows
print(data.head())

# Display information about the dataset
data.info()

# Display number of rows and columns
print("Shape:", data.shape)

print("\n Missing values:")
print(data.isnull().sum())

print("\n Number of duplicate values:")
print(data.duplicated().sum())


category_revenue = data.groupby("category")["total_price"].sum()

print("\nTotal revenue by category:")
print(category_revenue)

# Sort data by multiple columns
sorted_data = data.sort_values(
    by=["category", "total_price"],
    ascending=[True, False]
)

print("\nData sorted by category and total price:")
print(sorted_data.head(10))


# Create correlation matrix
correlation = data[["quantity", "unit_price", "total_price"]].corr()

print("\nCorrelation Matrix:")
print(correlation)