import pandas as pd

t_t_t = pd.DataFrame({
    "tick": ["X", "O", 'O'], 
    "tack": ["O", "O", 'X'], 
    "toe": ["O", "X", 'O'],
}, index=['tick', 'tack', 'toe'])

print(t_t_t.sort_index().sort_index(axis=1))
