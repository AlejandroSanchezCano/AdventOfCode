'''
--- Day 1.1: Secret Entrance ---
Iterate over rotations and use modulo 100 to keep the dial within 0-99
range. Increment password each time the dial hits 0.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    rotations = f.read().splitlines()

dial = 50
password = 0
for rotation in rotations:
    sign = 1 if rotation[0] == 'R' else -1
    turning = int(rotation[1:]) * sign
    dial += turning
    dial %= 100
    password += not dial
    
print(password)
