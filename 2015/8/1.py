'''
--- Day 8.1: Matchsticks ---
Don't construct the new strings, use eval!
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    strings = f.read().splitlines()

result = 0
for string in strings:
    result += len(string) - len(eval(string))
print(result)