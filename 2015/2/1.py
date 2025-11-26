'''
--- Day 2.1: I Was Told There Would Be No Math ---
Iteration over array and apply function per element.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    boxes = f.read().splitlines()

wrapping_paper = lambda l,w,h: 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
square_feet = [wrapping_paper(*map(int, box.split('x'))) for box in boxes]
print(sum(square_feet))