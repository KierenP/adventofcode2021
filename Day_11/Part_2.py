state = []

with open("Input.txt", "r") as file:
    for line in file:
        state.append([ int(x) for x in line.strip() ])

neighbours = { (0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1) }
answer = 0
step = 1

while True:
    for y, row in enumerate(state):
        for x, val in enumerate(row):
            state[y][x] += 1

    complete = False
    flashed = set()

    while not complete:
        complete = True
        for y, row in enumerate(state):
            for x, val in enumerate(row):
                if (x, y) not in flashed and val > 9:
                    complete = False
                    flashed.add((x, y))

                    for neighbour in neighbours:
                        new_x = x + neighbour[0]
                        new_y = y + neighbour[1]

                        if (new_x >= 0 and new_x < len(state[y]) and new_y >= 0 and new_y < len(state)):
                            state[new_y][new_x] += 1

    for y, row in enumerate(state):
        for x, val in enumerate(row):
            if state[y][x] > 9:
                state[y][x] = 0

    if len(flashed) == len(state) * len(state[0]):
        print(step)
        break

    step += 1
