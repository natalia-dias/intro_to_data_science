# from sklearn.dummy import DummyRegressor
from sklearn import datasets


# dummy_regressor = DummyRegressor(strategy='median')
X, y = datasets.load_boston(return_X_y=True)