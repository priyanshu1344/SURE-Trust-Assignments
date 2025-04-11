import pandas as pd
import numpy as np

#1
df = pd.read_csv('Titanic-Dataset.csv') 
data = df[['Age', 'Fare', 'Survived']]
data = data.dropna()
arr = data.to_numpy() #convert into numpy

#2
age = arr[:, 0]
fare = arr[:, 1]
age_norm = (age - age.mean()) / age.std() #Normalize age and fare
fare_norm = (fare - fare.mean()) / fare.std()

#3
survived = arr[:, 2]
mean_age_survived = age[survived == 1].mean() #Compute average age and fare for survived
mean_fare_survived = fare[survived == 1].mean()
mean_age_not_survived = age[survived == 0].mean() # for not survived
mean_fare_not_survived = fare[survived == 0].mean()

#4
fare_class = np.where(fare < fare.mean(), 'Low', 'High') # Use np.where()

#5
print("First 5 normalized ages:", age_norm[:5])
print("First 5 normalized fares:", fare_norm[:5])
print("\n Average for those who survived:")
print("Age:",mean_age_survived)
print("Fare:",mean_fare_survived)
print("\n Average for those who did not survive:")
print("Age:", mean_age_not_survived)
print("Fare:", mean_fare_not_survived)
print("\n First 10 fare labels (Low/High):", fare_class[:10])



