'''
--- Day 11.1: Corporate Policy ---
Build logic for password iteration and validate each geenrated password.
'''

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    password = f.read()

def valid(password):
    # Specific length
    if len(password) != 8: 
        return False
    # Lowercase
    if not password.islower(): 
        return False
    # Forbidden characters
    if 'i' in password: return False
    if 'o' in password: return False
    if 'l' in password: return False
    # Increasing straight
    ords = [ord(char) for char in password]
    diffs = [ords[idx+1] - ords[idx] for idx in range(len(ords) - 1)]
    current = 0
    longest = 0
    for d in diffs:
        if d != 1: 
            longest = max(current, longest)
            current = 0
        else:
            current += 1
    longest = max(current, longest)
    if longest < 2:
        return False
    # Two pairs
    seq = [diffs[0]]
    for diff in diffs:
        if diff != seq[-1]:
            seq.append(diff)
    zeros = [elem == 0 for elem in seq]
    if sum(zeros) < 2:
        return False
    # All conditions met
    return True

def next_password(password):
    if password[-1] != 'z':
        next_char = chr(ord(password[-1]) + 1)
        
        if next_char in ('i', 'o', 'l'):
            next_char = chr(ord(next_char) + 1)
        return password[:-1] + next_char
    else:
        for idx, char in enumerate(password[::-1]):
            if char != 'z': break
        aes = 'a' * idx
        idx = 8 - idx - 1
        next_char = chr(ord(password[idx]) + 1)
        if next_char in ('i', 'o', 'l'):
            next_char = chr(ord(next_char) + 1)
        password = password[:idx] + next_char + aes
        return password

# Main
password = 'vzbxxyzz'
while True:
    password = next_password(password)
    if valid(password):
        break
print(password)

