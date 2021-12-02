data = []

for line in open("Input.txt", "r"):
    data.append(int(line))

answer = sum(data[n] > data[n-3] for n in range(3,len(data)))

print(answer - 1)