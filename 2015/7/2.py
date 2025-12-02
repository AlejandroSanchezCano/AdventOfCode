'''
--- Day 7.1: Some Assembly Required ---
Repeat part 1 updating b's cable value and disregarding instruction without
operators like "19138 -> b"
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    instructions = f.read().splitlines()

class Instruction:

    def __init__(self, instruction: str):
        self.instruction = instruction
        left, output = instruction.split(' -> ')
        split = left.split(' ')
        self.output = output
        if len(split) == 1:
            self.operator = None
            self.main_input = int(split[0]) if self.output != 'a' else split[0]
            self.second_input = None
        elif len(split) == 2:
            self.operator = 'NOT'
            self.main_input = split[1]
            self.second_input = None
        else:
            self.operator = split[1]
            self.main_input = split[0] if not split[0].isdigit() else int(split[0])
            self.second_input = split[2] if not split[2].isdigit() else int(split[2])

    def __repr__(self):
        return self.instruction

    @staticmethod
    def __key(x):
        '''
        Ranking:
        1) None
        2) Integers
        3) 1-letter strings
        4) The rest
        '''
        if x is None: return (0, '')
        if isinstance(x, int): return (1, x)
        if len(x) == 1: return (2, x)
        return (3, x)

    def __lt__(self, other):
        # Simple connection
        if self.operator is None: return self.output != 'a'
        if other.operator is None: return other.output == 'a'
        # Bitwise operations
        input_data = [
            self.main_input, self.second_input, 
            other.main_input, other.second_input
            ]
        sorted_input = sorted(input_data, key = self.__key) 
        return sorted_input[-1] in (other.main_input, other.second_input)

    def connect(self):
        if self.operator is None:
            cables[self.output] = self.main_input if self.output != 'a' else cables[self.main_input]
        elif self.operator == 'NOT':
            cables[self.output] = 2**16 + ~cables[self.main_input]
        elif self.operator == 'RSHIFT':
            cables[self.output] = cables[self.main_input] >> int(self.second_input)
        elif self.operator == 'LSHIFT':
            cables[self.output] = cables[self.main_input] << int(self.second_input)
        else:
            value1 = cables[self.main_input] if self.main_input in cables else int(self.main_input)
            value2 = cables[self.second_input] if self.second_input in cables else int(self.second_input)
            if self.operator == 'AND':
                cables[self.output] = value1 & value2
            elif self.operator == 'OR':
                cables[self.output] = value1 | value2
            
cables = {}
instructions = [Instruction(instruction) for instruction in instructions]
for instruction in sorted(instructions):
    instruction.connect()
cables['b'] = cables['a']
for instruction in sorted(instructions):
    if instruction.operator is None and instruction.output != 'a': continue
    instruction.connect()
print(cables['a'])