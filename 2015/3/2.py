'''
--- Day 3.2: Perfectly Spherical Houses in a Vacuum ---
Iterate over array and fill a dictionary.
'''

from collections import defaultdict

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    moves = f.read()

santa = (0,0)
robosanta = (0,0)
deliver = {
    '^': lambda coord: (coord[0], coord[1] - 1),
    '>': lambda coord: (coord[0] + 1, coord[1]),
    'v': lambda coord: (coord[0], coord[1] + 1),
    '<': lambda coord: (coord[0] - 1, coord[1]),
}
house2presents = defaultdict(int)
house2presents[santa] += 1
house2presents[robosanta] += 1
for idx in range(len(moves)//2):
    move1, move2 = moves[idx*2], moves[idx*2 + 1]
    santa = deliver[move1](santa)
    robosanta = deliver[move2](robosanta)
    house2presents[santa] += 1
    house2presents[robosanta] += 1
print(len(house2presents))
