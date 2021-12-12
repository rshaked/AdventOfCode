from collections import defaultdict
import numpy as np

def count_vents(vents):
    count = 0
    for i in range(maxx+1):
        for j in range(maxy+1):
            if vents[i,j] > 1:
                count += 1
    return count

vectors = []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        line = line.split(' -> ')
        pair1 = list(map(int, line[0].split(',')))
        pair2 = list(map(int, line[1].strip().split(',')))
        vectors.append([pair1, pair2])
    
print("vectors: ", vectors)

maxx = 0
maxy = 0
for vector in vectors:
    if vector[0][0] > maxx:
        maxx = vector[0][0]
    elif vector[1][0] > maxx:
        maxx = vector[1][0]
    if vector[0][1] > maxy:
        maxy = vector[0][1]
    elif vector[1][1] > maxy:
        maxy = vector[1][1]
print("Maxes: ",maxx, maxy)

vents = np.zeros((maxx+1, maxy+1))

for vector in vectors:
    if vector[0][0] == vector[1][0]: #vertical
        start, end = sorted([vector[0][1],vector[1][1]])
        for i in range(start, end+1):
            vents[vector[0][0],i] += 1
    elif vector[0][1] == vector[1][1]: #horizontal
        start, end = sorted([vector[0][0],vector[1][0]])
        for j in range(start, end+1):
            vents[j,vector[0][1]] += 1
    else:
        xcomp = vector[1][0] - vector[0][0]
        ycomp = vector[1][1] - vector[0][1]       
        if xcomp < 0:
            if ycomp < 0:
                for i in range(abs(xcomp)+1):
                    vents[vector[0][0]-i,vector[0][1]-i] += 1
            if ycomp > 0:
                for i in range(abs(xcomp)+1):
                    vents[vector[0][0]-i,vector[0][1]+i] += 1
        if xcomp > 0:
            if ycomp < 0:
                for i in range(abs(xcomp)+1):
                    vents[vector[0][0]+i,vector[0][1]-i] += 1
            if ycomp > 0:
                for i in range(abs(xcomp)+1):
                    vents[vector[0][0]+i,vector[0][1]+i] += 1
        
        

print(vents.transpose())

print("Vents > 2: ", count_vents(vents))
