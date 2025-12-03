'''
--- Day 23.1: Opening the Turing Lock ---
Model each instruction as an object, execute them, and choose the next 
instruction by jumping in the list as much offset units as calculated during
executions.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    lines = f.read().splitlines()

class Instruction:
    
    def __init__(self, instruction: str):
        self.instruction = instruction
        self.command = instruction[:3]
        if self.command == 'jmp':
            self.offset = int(instruction.split()[1])
        elif self.command in ('jie', 'jio'):
            self.register = instruction[4]
            self.offset = int(instruction.split(', ')[-1])
        else:
            self.register = instruction[4]
            self.offset = 1

    def __repr__(self):
        return str(self.instruction)

    def execute(self):
        if self.command == 'hlf':
            registers[self.register] //= 2
        elif self.command == 'tpl':
            registers[self.register] *= 3
        elif self.command == 'inc':
            registers[self.register] += 1
        elif self.command == 'jmp':
            return self.offset
        elif self.command == 'jie':
            if registers[self.register] % 2 == 0:
                return self.offset
        elif self.command == 'jio':
            if registers[self.register] == 1:
                return self.offset
        return 1

registers = {
    'a': 0,
    'b': 0,
    }

idx = 0
instructions = [Instruction(instruction) for instruction in lines]
while True:
    offset = instructions[idx].execute()
    idx += offset
    if idx >= len(instructions): 
        break

print(registers['b'])