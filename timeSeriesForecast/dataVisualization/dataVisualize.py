import os
import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import DataFrame

series = read_csv(os.path.join(os.path.dirname(__file__), "../dataCollection/fromPomber/csvData.csv"), header=0, parse_dates=[0], index_col=0, squeeze=True)
dataframe = DataFrame(series)
print(type(series))
print(series.head())

print(series['2020-1'])
print(series.max())
print(series.describe())
plt.plot(series)
plt.show()

