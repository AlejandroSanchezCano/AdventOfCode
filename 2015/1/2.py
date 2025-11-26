'''
--- Day 1.2: Not Quite Lisp ---

'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    instructions = f.read()

floor = 0
for idx, instruction in enumerate(instructions, start=1):
    floor += 1 if instruction == "(" else -1
    if floor == -1:
        print(idx)
        break
