import pandas as pd

df = pd.read_csv('/Users/ndias/PycharmProjects/Salary Prediction/Topics/Working with missing values/Count NaNs/data/dataset/input.txt')
print(df.isnull().sum())

