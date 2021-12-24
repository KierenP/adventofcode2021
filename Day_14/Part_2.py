from collections import Counter
from functools import lru_cache

with open("Input.txt", "r") as file:

    polymer = file.readline().strip()
    pairs = {}

    file.readline()

    for line in file:
        pair = line.strip().split(' -> ')
        pairs[tuple(pair[0])] = pair[1]

@lru_cache(maxsize=None)
def grow(sub_polymer, depth, max_depth):
    global cache

    freq = Counter()

    if depth == max_depth:
        return freq

    if sub_polymer in pairs:
        freq += grow((sub_polymer[0], pairs[sub_polymer]), depth + 1, max_depth)
        freq += grow((pairs[sub_polymer], sub_polymer[1]), depth + 1, max_depth)
        freq[pairs[sub_polymer]] += 1

    return freq

freq = Counter()
for i in range(0, len(polymer) - 1):
    freq += grow((polymer[i], polymer[i+1]), 0, 40)

for letter in polymer:
    freq[letter] += 1

print(max(freq.values()) - min(freq.values()))