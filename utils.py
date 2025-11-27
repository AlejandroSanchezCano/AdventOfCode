class Grid:

    dirs = {
        'N': lambda r, c, d: (r - d, c + 0),
        'NE': lambda r, c, d: (r - d, c + d),
        'E': lambda r, c, d: (r + 0, c + d),
        'SE': lambda r, c, d: (r + d, c + d),
        'S': lambda r, c, d: (r + d, c + 0),
        'SW': lambda r, c, d: (r + d, c - d),
        'W': lambda r, c, d: (r + 0, c - d),
        'NW': lambda r, c, d: (r - d, c - d),
    }

    def __init__(self, grid):
        self.grid = grid
        self.nr = len(grid)
        self.nc = len(grid[0])
        self.directions = list(self.dirs)

    def __str__(self):
        return str(self.grid)

    def __call__(self, r, c = None):
        """What symbol occupies the cell (r, c)?"""
        # grid(0,0) vs grid((0,0))
        if c is None:
            r, c = r
        # list of lists vs numpy array
        if isinstance(self.grid, list): 
            return self.grid[r][c]
        else:
            return self.grid[r,c]

    def on_grid(self, r, c=None):
        """Is the cell (r, c) within the bounds?"""
        if c is None:
            r, c = r
        return 0 <= r < self.nr and 0 <= c < self.nc

    def is_edge(self, r, c=None):
        """Is the cell (r, c) on the edge?"""
        if c is None:
            r, c = r
        return r == 0 or r == self.nr - 1 or c == 0 or c == self.nc - 1

    def is_corner(self, r, c=None):
        """Is the cell (r, c) a corner?"""
        if c is None:
            r, c = r
        return (r == 0 and c == 0) or (r == 0 and c == self.nc - 1) or \
               (r == self.nr - 1 and c == 0) or (r == self.nr - 1 and c == self.nc - 1)

    def cells(self):
        """Iterates over the cells"""
        for r in range(self.nr):
            for c in range(self.nc):
                yield r, c

    def find(self, symbol):
        """What cell has a specific symbol?"""
        for cell in self.cells():
            if self(cell) == symbol:
                return cell
        return 'Not found'

    def modify(self, cell, symbol):
        """Modify the symbol at a specific cell"""
        if isinstance(self.grid, list):
            self.grid[cell[0]][cell[1]] = symbol
        else:
            self.grid[cell[0], cell[1]] = symbol

    def neighbors(self, r, c=None, directions = None, distance = 1, exclude_current = True):
        '''Return neighbor cells at a specific distance in specific directions'''
        if c is None: r, c = r
        if directions is None: directions = self.directions
        moves = [move for direction, move in self.dirs.items() if direction in directions]

        for move in moves:
            line = []
            for dist in range(exclude_current, distance + 1):
                next = move(r, c, dist)
                line += [(next)] if self.on_grid(*next) else []

            if len(line) == distance + (not exclude_current):
                yield line

    def around(self, r, c=None, directions=None):
        """Return the immediate neighbors"""
        if c is None: r, c = r
        if directions is None: directions = self.directions
        for direction in directions:
            move = self.dirs[direction]
            next = move(r, c, 1)
            if self.on_grid(*next):
                yield next

    def around_nobounds(self, r, c=None, directions=None):
        """Return the immediate neighbors without checking for out of bounds"""
        if c is None: r, c = r
        if directions is None: directions = self.directions
        for direction in directions:
            move = self.dirs[direction]
            next = move(r, c, 1)
            yield next

if __name__ == '__main__':
    import numpy as np
    grid = Grid(np.zeros((10,10)))
    print(grid.__dict__)
    print(grid(0,0))
    print(grid.on_grid((0,0)))
    print(grid.is_edge((0,5)))
    print(grid.is_corner((0,9)))