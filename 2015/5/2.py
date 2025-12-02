'''
--- Day 5.2: Doesn't He Have Intern-Elves For This? ---
Iteration over array and cheking for requirements.
'''

import itertools
from collections import defaultdict

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    strings = f.read().splitlines()

def xyx(string: str) -> bool:
    for idx in range(len(string) - 2):
        if string[idx] == string[idx + 2]:
            return True
    return False

def xyxy(string: str) -> bool:
    pair2indices = defaultdict(list)
    for idx, (char1, char2) in enumerate(itertools.pairwise(string)):
        pair = char1 + char2
        pair2indices[pair].append(idx)
    repeated_pairs = []
    for pair, indices in pair2indices.items():
        if len(indices) == 1: continue
        for index1 in indices:
            for index2 in indices:
                if abs(index2 - index1) > 1:
                    repeated_pairs.append(pair)
    return bool(repeated_pairs)

valid = 0
for string in strings:
    valid += xyx(string) and xyxy(string)
print(valid)