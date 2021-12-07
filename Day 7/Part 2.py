with open("Input.txt") as file:
    line = file.readline()
    line = line.split(',')
    line = [ int(x) for x in line ]

cost = [0] * (max(line) + 1 - min(line))

for crab in line:
    for index in range(0, len(cost)):
        cost[index] = cost[index] + int(abs(index - crab) * (abs(index - crab) + 1) / 2)

print(min(cost))
