'''
--- Day 5.1: Cafeteria ---
Iterate over all ingredient IDs and see if they are within in any fresh range.
If so, increment the fresh counter and break to the next ID.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    fresh_ranges, IDs = f.read().split('\n\n')
    IDs = map(int, IDs.split())
    fresh_ranges = [list(map(int, r.split('-'))) for r in fresh_ranges.split()]

fresh = 0
for ID in IDs:
    for fresh_range in fresh_ranges:
        if fresh_range[0] <= ID <= fresh_range[1]:
            fresh += 1
            break

print(fresh)