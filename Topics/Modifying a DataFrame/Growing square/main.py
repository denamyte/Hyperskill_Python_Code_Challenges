import pandas as pd

df = pd.DataFrame({'a': [1, 4], 'b': [2, 5]})

df['c'] = [3, 6]
df2 = pd.DataFrame({'a': [7], 'b': [8], 'c': [9]})
df = pd.concat([df, df2], ignore_index=True)
