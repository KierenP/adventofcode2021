
count = 0

with open("Input.txt") as file:
    for line in file:
        line = line.split("|")[1].split()

        word_lengths = [2, 3, 4, 7]

        for word in line:
            if len(word) in word_lengths:
                count = count + 1

print(count)
            


