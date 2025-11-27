'''
--- Day 8.2: Matchsticks ---
Don't construct the new strings, account for extra characters
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    strings = f.read().splitlines()

result = 0
for string in strings:
    total = 2
    for char in string:
        if char == '"': total += 1
        if char == '\\': total += 1
        total += 1
    result += total - len(string)
print(result)