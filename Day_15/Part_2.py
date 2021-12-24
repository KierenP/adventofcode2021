
from heapq import heappop
from heapq import heappush

risk = {}

with open("Input.txt", "r") as file:
    lines = file.readlines()

    size_x = len(lines[0].strip())
    size_y = len(lines)

    for y, line in enumerate(lines):
        for x, val in enumerate(line.strip()):
            for a in range(0, 5):
                for b in range(0, 5):
                    risk[(x + size_x * a, y + size_y * b)] = sum(map(int, str(int(val) + a + b)))

queue = [(0, (0, 0))]
complete = {}
visited = set()
neighbours = { (-1, 0), (1, 0), (0, 1), (0, -1) }

while len(queue) > 0:
    dist, node = heappop(queue)
    complete[node] = dist

    for neighbour in neighbours:
        next_node = (node[0] + neighbour[0], node[1] + neighbour[1])

        if next_node[0] >= 0 and next_node[0] < size_x * 5 and next_node[1] >= 0 and next_node[1] < size_y * 5:
            if next_node not in complete or complete[next_node] > dist + risk[next_node]:
                complete[next_node] = dist + risk[next_node] 
                heappush(queue, (dist + risk[next_node], next_node))  

print(complete[(size_x*5-1, size_y*5-1)] - complete[(0, 0)])
