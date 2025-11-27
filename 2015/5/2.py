'''
--- Day 5.2: Doesn't He Have Intern-Elves For This? ---
Iteration over array and cheking for requirements.
'''

import itertools
from collections import defaultdict

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    strings = f.read().splitlines()

#strings =['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'aaa']

valid = 0
for string in strings:
    inbetween = False
    pair2indices = defaultdict(list)
    for idx, (char1, char2) in enumerate(itertools.pairwise(string)):
        pair = char1 + char2
        pair2indices[pair].append(idx)
        # Check for letters with one letter between
        if idx < len(string) - 2 and string[idx] == string[idx + 2]:
            inbetween = True

    # Check for consecutive pairs
    consecutive = True
    for pair, indices in pair2indices.items():
        if len(indices) == 1: continue
        consecutive = any([
            indices[idx] - indices[idx - 1] == -1
            for idx in range(1, len(indices))
            ])
        if consecutive: break

    valid += inbetween and not consecutive
    print(inbetween, not consecutive)

print(valid)