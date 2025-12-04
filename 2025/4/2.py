'''
--- Day 4.2: Printing Department ---
Same as day 1 but repat the process iteratively.
'''

import scipy
import numpy as np

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    grid = np.array([list(line) for line in f.read().splitlines()])

total = 0
grid = grid == '@'
kernel = np.array([[1,1,1], [1,0,1], [1,1,1]])
while True:
    conv = scipy.signal.convolve2d(grid, kernel, mode='same')
    removed = (conv < 4) & (grid == 1)
    grid = grid & (~removed)
    total += removed.sum()
    if not removed.sum():
        break

print(total)