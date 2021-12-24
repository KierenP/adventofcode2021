import statistics

expected_brace = { '(' : ')', '{' : '}', '[' : ']', '<' : '>' }
score = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }

scores = []

with open("Input.txt", "r") as file:
    for line in file:
        stack = []
        
        for char in line.strip():
            if char in expected_brace:
                stack.append(char)
                continue
            
            expected = expected_brace[stack.pop()]

            if char != expected:
                break

        else:
            points = 0
            for char in reversed(stack):
                points = points * 5 + score[expected_brace[char]]

            scores.append(points)

print(int(statistics.median(scores)))
            
                