freq = [0] * 12
count = 0

for line in open("Input.txt"):
    for n in range(0, 12):
        freq[n] = freq[n] + int(line[n]) 

    count = count + 1

for n in range(0, 12):
    freq[n] = int(freq[n] * 2 > count)

gamma = sum(val*(2**idx) for idx, val in enumerate(reversed(freq)))
epsilon = sum((1-val)*(2**idx) for idx, val in enumerate(reversed(freq)))

print(gamma * epsilon)