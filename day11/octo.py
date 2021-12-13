import numpy as np
    
# read 2d matrix in simput.txt into an np array of digits
arraylines = []
with open("simput.txt") as f:
    lines = f.readlines()
    for line in lines:
        arraylines.append(list(map(int, str(line.strip()))))

array = np.array(arraylines)
print(array)

answer = 0

sha = array.shape

def flash(r,c):
    global answer
    global array
    answer += 1
    array[r][c] = -1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            rx = r+i
            cy = c+j
            if 0<=rx<sha[0] and 0<=cy<sha[1] and array[rx][cy]!=-1:
                array[rx][cy] += 1
                if array[rx][cy] == 10:
                    flash(rx,cy)

t = 0
while True:
    t += 1
    array = array + 1
    for i in range(sha[0]):
        for j in range(sha[1]):
            if array[i][j] == 10:
                flash(i,j)
    done = True
    for i in range(sha[0]):
        for j in range(sha[1]):
            if array[i][j] == -1:
                array[i][j] = 0
            else:
                done = False
    if t == 100:
        print("answer: ", answer)
    if done:
        print(t)
        break