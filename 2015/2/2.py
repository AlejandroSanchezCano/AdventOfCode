'''
--- Day 2.2: I Was Told There Would Be No Math ---
Iteration over array and apply function per element.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    boxes = f.read().splitlines()

ribbon = lambda d1,d2,d3: d1*d2*d3 + (d1+d2)*2
boxes = (sorted(map(int, box.split('x'))) for box in boxes)
feet = [ribbon(*box) for box in boxes]
print(sum(feet))
