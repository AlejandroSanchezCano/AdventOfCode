'''
--- Day 1.2: Secret Entrance ---
Iterate over rotations and use modulo 100 to keep the dial within 0-99
range. Increment password each time the dial hits 0 and for each full 
rotation over 0, recorded using remainder division. This creates a
problem when going from 0 to negative (extra count) or from positive to 
0 (extra count), so we correct for those cases.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    rotations = f.read().splitlines()

dial = 50
password = 0
for rotation in rotations:
    # Parse rotation
    sign = 1 if rotation[0] == 'R' else -1
    turning = int(rotation[1:]) * sign
    # Correct for 0 -> negative
    if not dial and sign == -1:
        password -= 1
    # Apply rotation
    dial += turning
    # Count full rotations
    password += abs(dial // 100)
    # Modulo to keep in range
    dial %= 100
    # Check for hitting 0
    password += not dial
    # Correct for positive -> 0
    if not dial and sign == 1:
        password -= 1
    
print(password)

