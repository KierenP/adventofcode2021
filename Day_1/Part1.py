data = []

for line in open("Input.txt", "r"):
    data.append(int(line))

answer = sum(data[n] > data[n-1] for n in range(1,len(data)))

print(answer)