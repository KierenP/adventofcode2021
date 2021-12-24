state = [0] * 9

with open("Input.txt") as file:
    line = file.readline()
    line = line.split(',')

    for fish in line:
        state[int(fish)] = state[int(fish)] + 1

def get_next_state(state):
    next_state = [0] * 9

    for index in range(0, 8):
        next_state[index] = state[index + 1]

    next_state[8] = state[0]
    next_state[6] = next_state[6] + state[0]

    return next_state

for days in range(0, 80):
    state = get_next_state(state)

print(sum(state))