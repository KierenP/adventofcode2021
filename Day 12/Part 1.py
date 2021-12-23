
connections = {}

with open("Input.txt", "r") as file:
    for line in file:
        caves = line.strip().split('-')
        connections.setdefault(caves[0], set())
        connections[caves[0]].add(caves[1])

        connections.setdefault(caves[1], set())
        connections[caves[1]].add(caves[0])

paths = 0

def next_node(path, current_cave):
    global paths

    for next_cave in connections[current_cave]:
        if next_cave == 'end':
            paths += 1 
        elif next_cave.isupper() or next_cave not in path:
            next_node(path + [next_cave], next_cave)

next_node(['start'], 'start')

print(paths)