'''
--- Day 3.1: Perfectly Spherical Houses in a Vacuum ---
Iterate over array and fill a dictionary.
'''

from collections import defaultdict

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    moves = f.read()

position = (0,0)
deliver = {
    '^': lambda coord: (coord[0], coord[1] - 1),
    '>': lambda coord: (coord[0] + 1, coord[1]),
    'v': lambda coord: (coord[0], coord[1] + 1),
    '<': lambda coord: (coord[0] - 1, coord[1]),
}
house2presents = defaultdict(int)
house2presents[position] += 1
for move in moves:
    position = deliver[move](position)
    house2presents[position] += 1
print(len(house2presents))
