'''
--- Day 6.2: Probably a Fire Hazard ---
Iterate over array and using numpy to apply binary operations.
'''

import re
import numpy as np

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    instructions = f.read().splitlines()

lights = np.zeros((1000, 1000))
for instruction in instructions:
    # Parse
    digits = re.findall('\d+', instruction)
    r1 = int(digits[0])
    c1 = int(digits[1])
    r2 = int(digits[2]) + 1
    c2 = int(digits[3]) + 1
    
    # Logic
    if 'turn on' in instruction:
        lights[r1:r2, c1:c2] += 1
    elif 'turn off' in instruction:
        decrease_bright = np.vectorize(lambda x: x-1 if x else x)
        lights[r1:r2, c1:c2] = decrease_bright(lights[r1:r2, c1:c2])
    elif 'toggle' in instruction:
        lights[r1:r2, c1:c2] += 2

print(int(lights.sum()))