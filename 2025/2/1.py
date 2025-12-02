'''
--- Day 2.1: Gift Shop ---
Brute-force solution where the odd-length IDs are skipped because they can't
possibly be invalid IDs, while the even-length IDs are splitted in half and
compared directly. The simplest solution is using regex ('^(.+)\1$') but it is
not as fast.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    product_ranges = f.read().rstrip().split(',')

invalid = []
for product_range in product_ranges:
    # Discard odd-length IDs
    start, end = product_range.split('-')
    lengths = (len(start), len(end))
    odds = (len(start) % 2 != 0, len(end) % 2 != 0)
    if all(odds): continue
    # Compare halves of wihtin-ranged IDs
    for ID in range(int(start), int(end) + 1):
        ID = str(ID)
        half1 = ID[:len(ID)//2]
        half2 = ID[len(ID)//2:]
        if half1 == half2:
            invalid.append(int(ID))
            
print(sum(invalid))