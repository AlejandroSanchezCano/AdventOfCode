'''
--- Day 13.1: Knights of the Dinner Table ---
Brute-force of all permutations. Could eb improved with DP
'''

import itertools
from collections import defaultdict

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    preferences = f.read().splitlines()

# Gather preferences
people = set()
company = defaultdict(dict)
for preference in preferences:
    split = preference.split()
    person1 = split[0]
    sign = split[2]
    hapiness = int(split[3]) if sign == 'gain' else -int(split[3])
    person2 = split[-1][:-1]
    company[person1][person2] = hapiness
    people.add(person1)
    people.add(person2)


# Brute force
table2hapiness = {}
for table in itertools.permutations(people):
    total_hapiness = 0
    table = tuple(list(table[-2:]) + list(table))
    for idx in range(1, len(table) - 1):
        middle = table[idx]
        left = table[idx - 1]
        right = table[idx + 1]
        total_hapiness += company[middle][left]
        total_hapiness += company[middle][right]
    table2hapiness[table] = total_hapiness

print(max(table2hapiness.values()))
        