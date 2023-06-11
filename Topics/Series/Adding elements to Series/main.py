import pandas as pd


m = {2021: 'Tokyo',
     2024: 'Paris',
     2028: 'Los Angeles'}


def add_records(olympics: pd.Series):
    for k, v in m.items():
        olympics[k] = v
    return olympics
