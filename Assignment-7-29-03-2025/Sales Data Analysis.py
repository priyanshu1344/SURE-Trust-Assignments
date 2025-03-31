import pandas as pd

sales_data = pd.DataFrame({
    "Product": ["MacBook Air", "Dell XPS 13", "iPhone 14", "Samsung Galaxy S23", "iPad Pro"],
    "Category": ["Laptop", "Laptop", "Smartphone", "Smartphone", "Tablet"],
    "Price": [999, 1199, 799, 899, 1099],
    "Units Sold": [35, 25, 50, 40, 30]
})

print("First 5 rows of the DataFrame:")
print(sales_data.head())

print("\nShape of the DataFrame (rows, columns):", sales_data.shape)
print("\nTotal number of elements in the DataFrame:", sales_data.size)
print("\nColumn names:", sales_data.columns.tolist())

print("\nMissing values in each column:")
print(sales_data.isnull().sum())

print("\nSummary statistics of numerical columns:")
print(sales_data.describe())
