def count_increases (lines):
    print(len(lines))
    prev_line = int(lines[0])
    increasing = 0
    for line in lines[1:]:
        if int(line) > prev_line:
            increasing += 1
        prev_line = int(line)
    return increasing

inputfile = open("input.txt", 'r')
lines = inputfile.readlines()
print(count_increases(lines))