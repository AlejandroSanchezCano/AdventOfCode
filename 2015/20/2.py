'''
--- Day 20.2: Infinite Elves and Infinite Houses ---
Same as part 1 but each elf stops after delivering presents to 50 houses, which
involves limiting the number of multiples a number is considered a divisor for.
'''

houses = 50
minimum = 33100000
upper_bound = minimum // 10
presents = lambda x: sum(divisors[x]) * 11

divisors = [[] for _ in range(upper_bound)]
for idx in range(1, upper_bound):
    for jdx in range(idx, min(upper_bound, idx * (houses + 1)), idx):
        divisors[jdx].append(idx)

    if presents(idx) >= minimum:
        break

print(idx)
