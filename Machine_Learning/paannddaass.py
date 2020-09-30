import pandas as pd

data = pd.read_csv("titanic.csv")

print(data.head())  # first 5 rows
print(data.tail())  # last 5 rowss

print(data.describe())  # statistics

# printing only specified column and this is called pandas series
print(data['Fare'])

# changing the column into boolean values
data['sex'] = data['Sex'] == 'male'  # creating new column
print(data.head())
arr = data[['Fare', 'Survived', 'Pclass']].values
print(arr)  # values in numpy arrays

print(arr[:, 2])
mask = arr[:, 2] < 2
print(arr[mask])
