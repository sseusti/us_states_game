import pandas
from pandas import read_csv

data = read_csv("Новая таблица - Лист1.csv")
data_df = pandas.DataFrame(data)

print(data_df)