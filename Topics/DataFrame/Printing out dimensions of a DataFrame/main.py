import pandas as pd

rows, cols = 0, 1


def print_dim(df: pd.DataFrame):
    shape = df.shape
    print(f'This DataFrame contains {shape[rows]} rows and {shape[cols]} columns')
