import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("../data/sales_data.csv")

# Create revenue column
data["Revenue"] = data["Quantity"] * data["Price"]

print("Dataset Preview:")
print(data.head())

# Total revenue
total_revenue = data["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Revenue by region
region_sales = data.groupby("Region")["Revenue"].sum()
print(region_sales)

# Plot sales by region
region_sales.plot(kind="bar", title="Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()
