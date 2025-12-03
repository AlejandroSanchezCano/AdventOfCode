'''
--- Day 3.2: Lobby ---
In every bank of batteries, we first need to find the position of the battery
with highest joltage. But not in the whole bank, because we need 12 digits. 
Instead, for the ith digit, we leave i - 1 trailing position and only search 
in the first section. Then, the bank gets reduced to the found position and
afterwards. For example, 1191111 -> 91111. This is repeated for every digit
position until we reach the last digit, in which case we take the maximum of
the remainding numbers, or the length of the trailing positions is equal
to the positions left to fill, in which case we just take them all.
To form the output joltage, take the joltage for each digit and calculate
joltage * 10 ** digit. This ensures that every unit (tens, hundreds, thousands,
...) is assigned correctly.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    banks = f.read().splitlines()

total = 0
digits = 12
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
