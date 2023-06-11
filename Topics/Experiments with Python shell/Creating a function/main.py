import math


# Modify this function in the shell and copy the new version here
def my_sqrt(value):
    t = type(value)
    return (math.sqrt(value)) if t in (int, float) \
        else 'The string should be converted into a numeric data type' if t == str  \
        else None
