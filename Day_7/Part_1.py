
with open("Input.txt") as file:
    line = file.readline()
    line = line.split(',')
    line = [ int(x) for x in line ]

cost = [0] * (max(line) + 1 - min(line))

for crab in line:
    for index in range(0, len(cost)):
        cost[index] = cost[index] + abs(index - crab)

print(min(cost))
