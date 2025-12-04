'''
--- Day 18.1: Like a GIF For Your Yard ---
Conway's game of life where iterations are implemented using convolutions.
'''

import scipy
import numpy as np

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    lights = np.array([list(line.strip()) for line in f.readlines()])

grid = lights == '#'
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
for _ in range(100):
    conv = scipy.signal.convolve2d(grid, kernel, mode='same')
    birth = (conv == 3) & ~grid
    survive = ((conv == 2) | (conv == 3)) & grid
    grid = birth | survive

print(grid.sum())
