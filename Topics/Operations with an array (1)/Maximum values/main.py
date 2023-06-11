import numpy as np

a = np.array([int(input()) for _ in range(3)])
print(a.max(), a.argmax(), sep='\n')
