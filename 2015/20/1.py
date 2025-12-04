'''
--- Day 20.1: Infinite Elves and Infinite Houses ---
Each house is visited by the elves that are divisors of the house number. So
we need to compute the divisors of the numbers in a big enough range and stop
when the sum of the divisors times 10 is at least the minimum number of 
presents. For that we need a very efficient way of computing divisors, so we
use something similar to the sieve of Eratosthenes, used to calculate prime 
numbers. It is essentially bottom-up dynamic programming (tabulation) => each 
number will be a divisor of itself, itself * 2, itself * 3, and so on.
This strategy is O(n log n), much faster than O(n^2) by double iteration, or
O(n sqrt n) by prime factorization.
'''

minimum = 33100000
upper_bound = minimum // 10
presents = lambda x: sum(divisors[x]) * 10

divisors = [[] for _ in range(upper_bound)]
for idx in range(1, upper_bound):
    for jdx in range(idx, upper_bound, idx):
        divisors[jdx].append(idx)

    if presents(idx) >= minimum:
        break

print(idx)

