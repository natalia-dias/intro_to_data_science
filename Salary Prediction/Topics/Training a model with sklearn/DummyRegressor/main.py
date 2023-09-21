#  write your code here
import pandas as pd
from sklearn.dummy import DummyRegressor

df = pd.read_csv('/Users/ndias/PycharmProjects/Salary Prediction/Topics/Training a model with sklearn/DummyRegressor/data/dataset/input.txt')
X_train = df['X']
y_train = df['y']

dummy_regr = DummyRegressor(strategy='quantile', quantile=0.4)
dummy_regr.fit(X_train, y_train)
print(round(dummy_regr.predict(X_train)[0], 4))
