
points = []

with open("Input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        coords = line.split(',')
        points.append((int(coords[0]), int(coords[1])))

    for line in file:
        instruction = line.strip().split()[-1]
        mirror = int(instruction.split('=')[1])

        if (instruction[0] == 'y'):
            for index, point in enumerate(points):
                if point[1] > mirror:
                    points[index] = (point[0], mirror - (point[1] - mirror))

        if (instruction[0] == 'x'):
            for index, point in enumerate(points):
                if point[0] > mirror:
                    points[index] = (mirror - (point[0] - mirror), point[1])

for i in range(0, max([p[1] for p in points]) + 1):
    for j in range(0, max([p[0] for p in points]) + 1):
        if (j, i) in points:
            print('#', end='')
        else:
            print(' ', end='')
    print()