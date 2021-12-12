from collections import deque


scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

keyed = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    score = 0
    for line in lines:
        # check for valid closing parentheses in lines using a deque
        d = deque()
        for char in line:
            if char in '({[<':
                d.append(char)
            else: # char in ')}]>':
                if d:
                    popped = d.pop()
                    # print(repr(popped), repr(char))
                    # print(popped == char)
                    if keyed[char] != popped:
                        score += scoring[char]
                        # print("line: {} score: {}".format(line, scoring[char]))
                        break
    print(score)