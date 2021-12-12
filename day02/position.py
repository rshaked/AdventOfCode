
def distance():
    hor = 0
    dep = 0
    for line in splitlines:
        if line[0] == "up":
            dep -= int(line[1])
        elif line[0] == "down":
            dep += int(line[1])
        elif line[0] == "forward":
            hor += int(line[1])
    return hor, dep

inputfile = open("input.txt", 'r')
lines = inputfile.readlines()
splitlines = [line.split(" ") for line in lines]
hor, dep = distance()
print(hor, dep)
print(hor*dep)