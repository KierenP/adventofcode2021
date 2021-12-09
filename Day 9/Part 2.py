import math

height_map = []

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        height_map.append([ int(h) for h in line ])

basin_count = 0
basins = {}

# make a dict where given a (x, y) we can look up what basin it is in
for y, row in enumerate(height_map):
    for x, height in enumerate(row):
        if ((x == 0                   or height_map[y][x-1] > height) and
            (x == len(row) - 1        or height_map[y][x+1] > height) and
            (y == 0                   or height_map[y-1][x] > height) and
            (y == len(height_map) - 1 or height_map[y+1][x] > height)):
            basins[(x, y)] = basin_count
            basin_count = basin_count + 1

# if you are next to a node in a basin and you aren't height 9, then you're in that basin
complete = False

while not complete:
    complete = True
    for y, row in enumerate(height_map):
        for x, height in enumerate(row):
            if (x, y) in basins:
                continue

            if (x-1, y) in basins and height != 9:
                basins[(x, y)] = basins[(x-1, y)]
                complete = False
            if (x+1, y) in basins and height != 9:
                basins[(x, y)] = basins[(x+1, y)]
                complete = False
            if (x, y-1) in basins and height != 9:
                basins[(x, y)] = basins[(x, y-1)]
                complete = False
            if (x, y+1) in basins and height != 9:
                basins[(x, y)] = basins[(x, y+1)]
                complete = False

basin_size = [0] * basin_count

for basin in basins.values():
    basin_size[basin] = basin_size[basin] + 1

print(math.prod(sorted(basin_size)[-3:]))