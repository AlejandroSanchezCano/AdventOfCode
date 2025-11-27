'''
--- Day 14.2: Reindeer Olympics ---
Use previous method on every second. Here the naïve approach of
calculating the distance each second would have worked.
'''

import re

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    reindeers = f.read().splitlines()

seconds = 2503
name2points = {reindeer.split()[0]: 0 for reindeer in reindeers}
for second in range(1, seconds + 1):
    name2distance = {name:0 for name in name2points}
    for reindeer in reindeers:
        # Parse
        speed, time, rest = [
            int(number) 
            for number in re.findall(r'\d+', reindeer)
            ]
        name = reindeer.split()[0]
        # Calculate distance
        cycles = second // (time + rest)
        remainder = second % (time + rest)
        distance = cycles * speed * time
        if remainder <= time:
            distance += speed * remainder 
        else:
            distance += speed * time 
        name2distance[name] = distance

    # There are no ties!
    winner = max(name2distance, key = name2distance.get)
    name2points[winner] += 1

print(max(name2points.values()))

