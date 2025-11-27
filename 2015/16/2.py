'''
--- Day 16.2: Aunt Sue ---
For every Sue, get the dictionary of what we remember of her, and apply 
the retroencabulator logic.
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    sues = f.readlines()

mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for sue in sues:
    split = re.split(r', |: ', sue.strip())
    number = int(split[0].split()[-1])
    sue = {}
    for idx in range(len(split[1:])//2):
        sue[split[1:][idx*2]] = int(split[1:][idx*2 + 1])

    for k in mfcsam:
        if k not in sue: continue
        if k in ('cats', 'trees'):
            if sue[k] <= mfcsam[k]: break
        elif k in ('goldfish', 'pomeranians'):
            if sue[k] >= mfcsam[k]: break
        else:
            if sue[k] != mfcsam[k]: break
    else:
        print(number)
        break