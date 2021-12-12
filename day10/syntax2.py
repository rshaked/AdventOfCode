from collections import deque


scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


keyed = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

keyed_reverse = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    scores = []
    for line in lines:
        # check for valid closing parentheses in lines using a deque
        d = deque()
        nope = False
        for char in line:
            if char in '({[<':
                d.append(char)
            else: # char in ')}]>':
                if d:
                    popped = d.pop()
                    if keyed[char] != popped:
                        nope = True
                        break
        score = 0
        if not nope:
            while d:
                popped = d.pop()
                score *= 5
                score += scoring[keyed_reverse[popped]]
            scores.append(score)
    print(scores)
    scores.sort()
    print(scores[len(scores)//2])