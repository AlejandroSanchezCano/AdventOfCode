'''
--- Day 4.2: The Ideal Stocking Stuffer ---
Brute-force search.
'''

import hashlib
from tqdm import tqdm
from itertools import count

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    secret_key = f.read()

for idx in tqdm(count()):
    tohash = secret_key + str(idx)
    md5 = hashlib.md5(tohash.encode())
    hexadecimal = md5.hexdigest()
    if hexadecimal[:6] == '000000':
        print(idx)
        break
