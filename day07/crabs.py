from collections import defaultdict

crabs = defaultdict(int)

with open("input.txt") as f:
    positions = f.readline().split(',')
    for position in positions:
        crabs[int(position)] += 1
    
# aim = round(sum(list(map(int, positions)))/len(positions))
# print(aim)
# diff = 0

# for position, num_of_crabs in crabs.items():
#     diff += abs(position - aim)*num_of_crabs

# print(diff)

# -------
diffs = {}
for loc in set(positions):
    diff = 0
    aim = int(loc)
    # print(aim)
    
    for position, num_of_crabs in crabs.items():
        # print("A: ",abs(position - aim)*num_of_crabs)
        diff += abs(position - aim)*num_of_crabs
    diffs[aim] = diff

print(diffs)

aim = min(diffs, key=diffs.get)
print(aim, " -> ",diffs[aim])