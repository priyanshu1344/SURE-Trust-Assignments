import pandas as pd

#1
df = pd.read_excel("iris.xlsx")

#2
df['petal.ratio'] = df['petal.length'] / df['petal.width']

#3
average_ratio = df.groupby('variety')['petal.ratio'].mean()
print("Average petal ratio for each species:\n", average_ratio)

#4
std_sepal = df.groupby('variety')['sepal.length'].std()
most_varied_species = std_sepal.idxmax()
print("\nSpecies with highest variation in sepal length:", most_varied_species)

#5
mean_sepal_width = df['sepal.width'].mean()
filtered_df = df[df['sepal.width'] > mean_sepal_width]
print("\nNumber of rows with sepal width > average:", filtered_df.shape[0])

#6
less_than_2 = df[df['petal.ratio'] < 2]
greater_equal_2 = df[df['petal.ratio'] >= 2]

combined_df = pd.concat([less_than_2, greater_equal_2])
print("\nCombined dataset shape after stacking:", combined_df.shape)
