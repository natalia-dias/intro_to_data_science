#  write your code here 
import pandas as pd


df = pd. read_csv('/Users/ndias/PycharmProjects/Data Analysis for Hospitals/Topics/Working with missing values/Calculate proportions of NaNs/data/dataset/input.txt')
result = round(df.isnull().sum() / df.shape[0], 2)
print(result)
