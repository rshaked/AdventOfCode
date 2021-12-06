from collections import defaultdict

fish = defaultdict(int)

with open('input.txt') as f:
    infish = list(map(int, f.read().split(',')))
    for f in infish:
        fish[f] += 1

print(fish)

for x in range(256):
    fishdiff = defaultdict(int)
    for key, value in fish.items():
        if key == 0:
            fishdiff[0] -= value
            fishdiff[8] += value
            fishdiff[6] += value
        else:
            fishdiff[key] -= value
            fishdiff[key-1] += value
    for key2, diff in fishdiff.items():
            fish[key2] += diff

print(fish)
print(sum(fish.values()))