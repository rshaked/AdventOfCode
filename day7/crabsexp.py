from collections import defaultdict


crabs = defaultdict(int)

with open("input.txt") as f:
    positions = f.readline().split(',')
    for position in positions:
        crabs[int(position)] += 1

positions = list(map(int, positions))
diffs = {}
for loc in range(max(positions)):
    diff = 0
    aim = loc
    
    for position, num_of_crabs in crabs.items():
        print("loc: ", loc)
        # print("pos: ", position, " num_of_crabs: ",num_of_crabs, sum(range(abs(position - aim))), " * ", num_of_crabs)
        n = abs(position - aim)+1
        nprime = (n*(n+1))/2
        diff += nprime*num_of_crabs
    diffs[aim] = diff

print(diffs)

aim = min(diffs, key=diffs.get)
print(aim, " -> ",diffs[aim])