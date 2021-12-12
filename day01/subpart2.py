def window_increases (lines):
    # print(len(lines))
    prev_window = (int(lines[0]),
                   int(lines[1]),
                   int(lines[2]))
    increasing = 0
    for i in range(1,len(lines)-2):
        current_window = (int(lines[i]),
                         int(lines[i+1]),
                         int(lines[i+2]))
        if sum(current_window) > sum(prev_window):
            increasing += 1
        prev_window = current_window
    return increasing

inputfile = open("input.txt", 'r')
lines = inputfile.readlines()
print(window_increases(lines))