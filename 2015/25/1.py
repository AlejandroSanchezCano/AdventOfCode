'''
--- Day 25.1: Let It Snow ---
Go from one code to the next one in the sequence is just a mutiplication and
a modulo division. This is semi-fast and repeated as many times as codes in the
sequence are, which is calculated from the row and columns.
- First strategy -> r and c form a rectangle and leave out two upper triangular
matrices of dimensions (r-1 x r-1) and (c-1 x c-1). Then, account for the
positions in the last layer of the sequence using c - 1.
- Second strategy -> the sequence forms a triangle in which each position marks
the layer it is in by (r + c - 1). Use that to calculate the area of the 
triangle (with the diagonal) and account for the extra positions added with 
min(r,c) + 1
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    r, c = map(int, re.findall(r'\d+', f.read()))

strat1 = lambda r, c: r*c + (r - 1)*(r - 2)/2 + (c - 1)*(c - 2)/2  + c - 1
strat2 = lambda r, c: (r+c-1)*(r+c)/2 - min(r,c) + 1

code = 20151125
for _ in range(int(strat2(r,c))-1):
    code *= 252533
    code %= 33554393
print(code)
