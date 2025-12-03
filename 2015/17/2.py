'''
--- Day 17.2: No Such Thing as Too Much ---
Same as day 1 but keeping track of the cups that are used at each part of the
problem by returning an empty list (of list) in the base cases, adding the
current cup to the list and merging the list of cups from the two avenues 
(taking or not taking the cup)
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    cups = list(map(int, f.read().splitlines()))

eggnog = 150

def combinations(total: int, idx: int) -> int:
    # Base case 1 -> right combination of cups
    if total == 0:
        return (1, [[]])
    
    # Base case 2 -> wrong combination of cups
    if total < 0 or idx == len(cups):
        return (0, [])

    # Two choices: use of not use the cup
    with_counts, with_cups = combinations(total - cups[idx], idx + 1)
    without_counts, without_cups = combinations(total, idx + 1)

    # Add cup to arrangement
    with_cups = [[cups[idx]] + cuplist for cuplist in with_cups]

    return (with_counts + without_counts), (with_cups + without_cups)

ways, combinations = combinations(eggnog, 0)
lengths = [len(combination) for combination in combinations]
count_minimum = sum(length == min(lengths) for length in lengths)
print(count_minimum)