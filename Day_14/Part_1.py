import collections

with open("Input.txt", "r") as file:

    polymer = file.readline().strip()
    pairs = {}

    file.readline()

    for line in file:
        pair = line.strip().split(' -> ')
        pairs[pair[0]] = pair[1]

for step in range(0, 10):
    next_polymer = []

    for i in range(0, len(polymer) - 1):
        pair = ''.join([polymer[i], polymer[i+1]])
        next_polymer.append(polymer[i])
        if pair in pairs:
            next_polymer.append(pairs[pair])

    next_polymer.append(polymer[-1])
    polymer = next_polymer

counter=collections.Counter(polymer)
print(max(counter.values()) - min(counter.values()))