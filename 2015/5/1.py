'''
--- Day 5.1: Doesn't He Have Intern-Elves For This? ---
Iteration over array and cheking for requirements.
'''

import itertools

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    strings = f.read().splitlines()

valid = 0
vowels = 'aeiou'
for string in strings:
    requirement_vowels = 0
    requirement_double = False
    requirement_substrings = True
    for char1, char2 in itertools.pairwise(string):
        if char1 in vowels:
            requirement_vowels += 1
        if char1 == char2:
            requirement_double = True
        elif char1+char2 in {'ab', 'cd', 'pq', 'xy'}:
            requirement_substrings = False
            break
    if string[-1] in vowels:
        requirement_vowels += 1

    requirements = (
        requirement_vowels > 2, 
        requirement_double, 
        requirement_substrings
        )
    valid += all(requirements)
    
print(valid)