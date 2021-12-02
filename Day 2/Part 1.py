position = 0
depth = 0

for line in open("Input.txt"):
    line = line.split()

    if (line[0] == "forward"):
        position = position + int(line[1])
    elif (line[0] == "down"):
        depth = depth + int(line[1])
    elif (line[0] == "up"):
        depth = depth - int(line[1])

print (position * depth)
