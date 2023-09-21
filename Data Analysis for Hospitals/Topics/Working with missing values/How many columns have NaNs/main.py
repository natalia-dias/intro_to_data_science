#  write your code here 
import pandas as pd
df = pd.read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/How many columns have NaNs/data/dataset/input.txt')
print(df.shape[1] - df.dropna(axis=1).shape[1])