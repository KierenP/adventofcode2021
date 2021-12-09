
height_map = []

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        height_map.append([ int(h) for h in line ])

answer = 0

for y, row in enumerate(height_map):
    for x, height in enumerate(row):
        if ((x == 0                   or height_map[y][x-1] > height) and
            (x == len(row) - 1        or height_map[y][x+1] > height) and
            (y == 0                   or height_map[y-1][x] > height) and
            (y == len(height_map) - 1 or height_map[y+1][x] > height)):
            answer = answer + height + 1

print(answer)