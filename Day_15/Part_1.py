
risk = {}

with open("Input.txt", "r") as file:
    lines = file.readlines()

    size_x = len(lines[0].strip())
    size_y = len(lines)

    for y, line in enumerate(lines):
        for x, val in enumerate(line.strip()):
            risk[(x, y)] = int(val)

queue = {}
complete = {}
queue[(0, 0)] = 0
neighbours = { (-1, 0), (1, 0), (0, 1), (0, -1) }

while len(queue) > 0:
    next_node = min(queue, key=queue.get)
    complete[next_node] = queue[next_node] + risk[next_node]
    queue.pop(next_node)

    for neighbour in neighbours:
        node = tuple(map(sum, zip(next_node, neighbour)))

        if node in complete:
            continue

        if node[0] >= 0 and node[0] < size_x and node[1] >= 0 and node[1] < size_y:
            if node in queue:
                queue[node] = min(queue[node], complete[next_node])
            else:
                queue[node] = complete[next_node]

print(complete[(size_x-1, size_y-1)] - complete[(0, 0)])
