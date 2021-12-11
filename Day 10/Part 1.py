
expected_brace = { '(' : ')', '{' : '}', '[' : ']', '<' : '>' }
score = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }

total = 0

with open("Input.txt", "r") as file:
    for line in file:
        stack = []
        for char in line.strip():
            if char in expected_brace:
                stack.append(char)
                continue
            
            expected = expected_brace[stack.pop()]

            if char != expected:
                total = total + score[char]
                break

print(total)
            
                
            
