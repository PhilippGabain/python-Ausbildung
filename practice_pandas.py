import pandas as pd

dataframe = pd.read_csv("global_air_quality_data_10000.csv", sep=',', header='infer', encoding=None)

print(dataframe.head())