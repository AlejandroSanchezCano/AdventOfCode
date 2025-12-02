'''
--- Day 2.2: Gift Shop ---
Brute-force solution where now regex is 3s faster than the naïve approach.
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    product_ranges = f.read().rstrip().split(',')

invalid = []
for product_range in product_ranges:
    start, end = product_range.split('-')
    for ID in range(int(start), int(end) + 1):
        if re.match(r'^(.+)\1+$', str(ID)):
            invalid.append(int(ID))
            
print(sum(invalid))
