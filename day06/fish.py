with open('input.txt') as f:
    fish = list(map(int, f.read().split(',')))

print(fish)
for x in range(256):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))