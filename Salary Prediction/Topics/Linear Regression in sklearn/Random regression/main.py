#  write your code here 
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# df = pd.read_csv("/Users/ndias/PycharmProjects/Salary Prediction/Topics/Linear Regression in sklearn/Random regression/data/dataset/input.txt")
# X_train = df.iloc[:-70,:4]
# X_test = df.iloc[-70:, :4]
# y_train = df.target[:-70]
# y_test = df.target[-70:]
#
# model = LinearRegression()
# model.fit(X_train, y_train)
# print(round(model.intercept_, 3))

df = pd.read_csv('/Users/ndias/Downloads/Новая таблица - Лист1.csv', header=0, names=['cost', 'customers'])
# Save table as .csv then import as pd or np array. Don't forget to change columns name.
X = np.array(df['cost']).reshape(-1, 1)
y = df['customers']
# df = pd.read_csv('')
# X = np.array([[4, 6, 8, 10, 12, 14, 16]]).reshape(-1, 1)
# X_test = np.array([23]).reshape(1, 1)
X_test = [[23]]
# y = np.array([[2, 2, 3, 5, 5, 6, 6]])
model = LinearRegression()
model.fit(X, y)
print(model.predict(X_test))
