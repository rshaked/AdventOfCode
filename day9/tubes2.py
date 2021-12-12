import numpy as np
from collections import defaultdict
from functools import reduce

# consume a file called "input.txt" and put the contents into a 2d numpy array
def consume_input(filename):
    with open(filename) as f:
        return np.array([list(line.strip()) for line in f], dtype=int)

input = consume_input("input.txt")
print(np.shape(input))
print(input)

ones = np.ones(input.shape, dtype=int)
for x in range(input.shape[0]):
    for y in range(input.shape[1]):
        if input[x,y] == 9:
            ones[x,y] = 0

array = ones
print(array)
def DFS(i, j):
    if i < 0 or i >= array.shape[0] or j < 0 or j >= array.shape[1] or array[i,j] != 1:
        return 0
    # mark it as visited
    array[i,j] = -1
    count = 1

    # Recur for 8 neighbours
    count += DFS(i - 1, j)
    count += DFS(i, j - 1)
    count += DFS(i, j + 1)
    count += DFS(i + 1, j)
    return count 


def countIslands():
    count = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i,j] == 1:
                count.append(DFS(i, j))

    # get the 3 biggest values from count
    count.sort(reverse=True)
    return reduce((lambda x, y: x * y),count[:3])



print(countIslands())

