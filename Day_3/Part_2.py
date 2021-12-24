
def binary_str_to_value(str):
    return int(str, 2)

with open("Input.txt") as f:
    lines = f.read().splitlines()
    count = len(lines)

    for n in range(0, 12):
        freq = 0

        for line in lines:
            freq = freq + int(line[n])

        more_frequent = int(freq * 2 >= len(lines))

        lines = [line for line in lines if int(line[n]) == more_frequent]

        if (len(lines) == 1):
            break

    global oxygen
    oxygen = binary_str_to_value(lines[0])

with open("Input.txt") as f:
    lines = f.read().splitlines()
    count = len(lines)

    for n in range(0, 12):
        freq = 0

        for line in lines:
            freq = freq + int(line[n])

        less_frequent = 1 - int(freq * 2 >= len(lines))

        lines = [line for line in lines if int(line[n]) == less_frequent]

        if (len(lines) == 1):
            break

    global co2
    co2 = binary_str_to_value(lines[0])

print(oxygen * co2)
