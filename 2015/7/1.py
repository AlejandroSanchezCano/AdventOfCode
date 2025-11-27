'''
--- Day 7.1: Some Assembly Required ---

'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    instructions = f.read().splitlines()

cables = {}

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
            self.main_input = split[0]
            self.second_input = split[2]

    def __repr__(self):
        return self.instruction

    @staticmethod
    def __compare(cable1, cable2):
        if len(cable1) != len(cable2):
            return len(cable1) < len(cable2)
        return cable1 < cable2

    #def __lt__(self, other):
    #    if self.operator is None: return self.output != 'a'
    #    if other.operator is None: return other.output == 'a'
    #    if self.second_input is None or 'SHIFT' in self.operator:
    #        return self.__compare(self.main_input, other.output)
    #    if other.second_input is None or 'SHIFT' in self.operator:
    #        return self.__compare(self.output, other.main_input)
    #    return self.__compare(self.main_input, other.output) \
    #        and self.__compare(self.second_input, other.output)

    def __lt__(self, other):
        if self.operator is None: return self.output != 'a'
        if other.operator is None: return other.output == 'a'
        if self.second_input is None or 'SHIFT' in self.operator:
            if self.main_input == other.output: return False
            return self.__compare(self.main_input, other.output)
        if other.second_input is None or 'SHIFT' in self.operator:
            if self.output == other.main_input: return True
            return self.__compare(self.output, other.main_input)
        return self.__compare(self.main_input, other.output) \
            and self.__compare(self.second_input, other.output)    
    def connect(self):
        if self.operator is None:
            cables[self.output] = self.main_input
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
                

instructions = [Instruction(instruction) for instruction in instructions]
for i in sorted(instructions):
    print(i)
#dsfdsf
#for i in sorted(instructions):
#    print(i)
#    i.connect()
#    #print(cables)