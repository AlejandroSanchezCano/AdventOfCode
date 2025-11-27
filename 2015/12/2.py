'''
--- Day 12.2: JSAbacusFramework.io ---
Parse through the lists and dicts and sum the numbers recursively.
'''

import json

with open(__file__.rsplit("/", 1)[0] + "/input.txt") as f:
    content = f.read()

data = json.loads(content)

def parse_list(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += parse_list(elem)
        elif isinstance(elem, dict):
            total += parse_dict(elem)
        elif isinstance(elem, int):
            total += elem
    return total

def parse_dict(d):
    total = 0
    for k, v in d.items():
        if v == 'red': return 0
        if isinstance(v, list):
            total += parse_list(v)
        elif isinstance(v, dict):
            total += parse_dict(v)
        elif isinstance(v, int):
            total += v
    return total

print(parse_list(data))