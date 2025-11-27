'''
--- Day 14.1: Reindeer Olympics ---
Don't calculate the distance after each second, but calculate it knowing
that the distance traveled by the reindeers is a stepwisefunction.
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    reindeers = f.read().splitlines()

seconds = 2503
distances = []
for reindeer in reindeers:
    # Parse
    speed, time, rest = [
        int(number) 
        for number in re.findall(r'\d+', reindeer)
        ]
    name = reindeer.split()[0]
    # Calculate distance
    cycles = seconds // (time + rest)
    remainder = seconds % (time + rest)
    distance = cycles * speed * time
    if remainder <= time:
        distance += speed * remainder 
    else:
        distance += speed * time 
    distances.append(distance)

print(max(distances))
