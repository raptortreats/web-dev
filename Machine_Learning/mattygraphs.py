import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('titanic.csv')
print(data.head())

plt.scatter(data['Age'], data['Fare'])

plt.plot([0, 80], [85, 5])
