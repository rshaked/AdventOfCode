import numpy as np

# consume a file called "input.txt" and put the contents into a 2d numpy array
def consume_input(filename):
    with open(filename) as f:
        return np.array([list(line.strip()) for line in f])

input = consume_input("input.txt")
print(np.shape(input))
print(input)



# take a 2d array and compare every element to its neighbors
def compare_neighbors(array, x, y):
    width, length = np.shape(array)
    low = True
    curr = array[x][y]
    if x > 0:
        if array[x-1][y] <= curr:
            low = False
    if x < width-1:
        if array[x+1][y] <= curr:
            low = False
    if y > 0:
        if array[x][y-1] <= curr:
            low = False
    if y < length-1:
        if array[x][y+1] <= curr:
            low = False
    return low

width, length = np.shape(input)
lows = []
risks = []
count = 0
for x in range(width):
    for y in range(length):
        if compare_neighbors(input, x, y):
            lows.append((x,y))
            risks.append(int(input[x][y])+1)
            count += 1
            print(x, y)

print(count)
print(lows)
print("sum:", sum(risks))