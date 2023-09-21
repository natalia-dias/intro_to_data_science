import pandas as pd

def create_series(foods, calories):
    calorie_content = pd.Series(calories, index=foods, name="Calorie content")
    return calorie_content
