import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Calculate total revenue by category
category_revenue = data.groupby("category")["total_price"].sum()

# Create bar chart
plt.figure(figsize=(8, 5))
category_revenue.plot(kind="bar")

plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()