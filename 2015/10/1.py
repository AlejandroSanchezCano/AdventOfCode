'''
--- Day 10.1: Elves Look, Elves Say ---
In every iteration, get the stretch of consecutive characters and build
the new sequence taking into account that there cannot appear a
character higher than in the inital sequence (according to Wikipedia)
https://en.wikipedia.org/wiki/Look-and-say_sequence
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    sequence = f.read()

rule = {
    '1': '11',
    '11': '21',
    '111': '31',
    '2': '12',
    '22': '22',
    '222': '32',
    '3': '13',
    '33': '23',
    '333': '33'
}

limit = 40
for _ in range(limit):
    # Determine groups of consecutive characters
    groups = []
    stretch = sequence[0]
    for char in sequence[1:]:
        if char in stretch: 
            stretch += char
        else: 
            groups.append(stretch)
            stretch = char
    groups.append(stretch)
    
    # Generate new sequence
    sequence = ''.join([rule[group] for group in groups])

print(len(sequence))