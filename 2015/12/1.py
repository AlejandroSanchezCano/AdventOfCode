'''
--- Day 12.1: JSAbacusFramework.io ---
Get numbers with regex.
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    content = f.read()

total = sum(map(int, re.findall(r"-?\d+", content)))
print(total)