import pandas as pd

def create_series(capitals):
    cap_series = pd.Series(capitals, name='Capitals of the world')
    return cap_series
