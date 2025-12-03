'''
--- Day 3.1: Lobby ---
Simpler case of part 2.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    banks = f.read().splitlines()

total = 0
digits = 2
for bank in banks:
    maximum = 0
    for idx in range(digits, 0 , -1):
        if len(bank) == idx: 
            maximum += int(bank)
            break
        if idx == 1:
            maximum += int(max(set(bank)))
            break
        indices = sorted(range(len(bank[:-idx+1])), key = lambda x: bank[x], reverse = True)
        maximum += int(bank[indices[0]]) * 10 ** (idx - 1)
        bank = bank[indices[0] + 1:]
    total += maximum
print(total)
