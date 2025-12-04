'''
--- Day 4.1: Printing Department ---
Transform the grid to binary values and perform convolutions.
'''

import scipy
import numpy as np

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

grid = grid == '@'
kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
conv = scipy.signal.convolve2d(grid, kernel, mode='same')
remove = (conv < 4) & (grid == 1)
print(remove.sum())