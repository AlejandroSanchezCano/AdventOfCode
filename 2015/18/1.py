'''
--- Day 18.1: Like a GIF For Your Yard ---
Game of life
'''
import utils
import numpy as np

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    lights = [list(line.strip()) for line in f.readlines()]

grid = utils.Grid(np.array(lights))

@np.vectorize
def switch(r, c):
    if grid.is_corner((r, c)): return '#'
    on = sum([grid(neighbor) == '#' for neighbor in grid.around(r, c)])
    if grid(r, c) == '#':
        return '#' if on in (2, 3) else '.'
    else:
        return '#' if on == 3 else '.'

I, J = np.indices(grid.grid.shape)
print(grid.grid)
for _ in range(100):
    grid.grid = switch(I, J)
print((grid.grid == '#').sum())