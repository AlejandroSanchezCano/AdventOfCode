'''
--- Day 1.1: Not Quite Lisp ---
Iteration over array.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    instructions = f.read()

ups_downs = [1 if instruction == "(" else -1 for instruction in instructions]
print(sum(ups_downs))