
digcount = 0
lenmap = {2:1, 4:4, 3:7, 7:8}

with open("input.txt") as f:
    inputs = f.readlines()
    for input in inputs:
        input_text = input.split(' | ')
        signals = list(map(str.strip,input_text[0].split(' ')))
        outputs = list(map(str.strip,input_text[1].split(' ')))
        for output in outputs:
            if len(output) in lenmap:
                digcount += 1 
        print(digcount)

    