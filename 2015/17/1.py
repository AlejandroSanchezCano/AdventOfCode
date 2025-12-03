'''
--- Day 17.1: No Such Thing as Too Much ---
Problem strikingly similar to the classical 'minimum coins needed', which 
involves dynamic programming to be solved, yet this variation, although
slightly benefits from memoization, does not have a lot of repeated
subproblems, so simply recursion does the  job.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    cups = list(map(int, f.read().splitlines()))

eggnog = 150

def combinations(total: int, idx: int) -> int:
    # Base case 1 -> right combination of cups
    if total == 0:
        return 1
    
    # Base case 2 -> wrong combination of cups
    if total < 0 or idx == len(cups):
        return 0

    # Two choices: use of not use the cup
    with_counts = combinations(total - cups[idx], idx + 1)
    without_counts = combinations(total, idx + 1)

    return with_counts + without_counts

print(combinations(eggnog, 0))