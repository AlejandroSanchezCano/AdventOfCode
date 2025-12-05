'''
--- Day 5.2: Cafeteria ---
Sort the fresh ranges by their start value and the iterate over the sorted 
ranges merging any overlapping ranges. Lastly, sum the lengths of the merged
ranges.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    fresh_ranges, IDs = f.read().split('\n\n')
    IDs = map(int, IDs.split())
    fresh_ranges = [list(map(int, r.split('-'))) for r in fresh_ranges.split()]

fresh_ranges = sorted(fresh_ranges, key = lambda x: x[0])

total = 0
current = fresh_ranges[0]
for bounds in fresh_ranges[1:]:
    # No overlap
    if bounds[0] > current[1]:
        total += current[1] - current[0] + 1
        current = bounds
    # Complete overlap
    elif bounds[0] >= current[0] and bounds[1] <= current[1]:
        continue
    # Partial overlap
    elif bounds[0] <= current[1]:
        current = [current[0], bounds[1]]
total += current[1] - current[0] + 1
print(total)