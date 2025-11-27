'''
--- Day 9.2: All in a Single Night ---
Brute force travelling salesman problem (TSP)
'''

import itertools

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    lines = f.read().splitlines()

cities2distance = {}
unique_cities = set()
for line in lines:
    cities, distance = line.split(' = ')
    city1, city2 = cities.split(' to ')
    unique_cities.add(city1)
    unique_cities.add(city2)
    cities = tuple(sorted([city1, city2]))
    cities2distance[cities] = int(distance)

path2distance = {}
for permutation in itertools.permutations(unique_cities, r=len(unique_cities)):
    distance = 0
    for cities in itertools.pairwise(permutation):
        cities = tuple(sorted(cities))
        distance += cities2distance[cities]
    path2distance[permutation] = distance
print(max(path2distance.values()))