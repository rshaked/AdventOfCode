from collections import defaultdict

# convert list of ints into one int
def convertlistofints(listofints):
    num = 0
    for i in listofints:
        num = num * 10 + i
    return num


sigmap = {"acedgfb": 8,
        "cdfbe": 5,
        "gcdfa": 2,
        "fbcad": 3,
        "dab": 7,
        "cefabd": 9,
        "cdfgeb": 6,
        "eafb": 4,
        "cagedb": 0,
        "ab": 1}
letterdicts = {}
for key, value in sorted(sigmap.items()):
    letterdict = defaultdict(int)
    for letter in key:
        letterdict[letter] += 1
    letterdicts[value] = letterdict
for key, value in sorted(letterdicts.items()):
    print(key, sorted(set(value)))
    print()

with open("input.txt") as f:
    inputs = f.readlines()
    nums = []
    for input in inputs:
        lenmap = {2:1, 4:4, 3:7, 7:8}
        maplen = {1:2, 4:4, 7:3, 8:7}
        input_text = input.split(' | ')
        signals = list(map(str.strip,input_text[0].split(' ')))
        outputs = list(map(str.strip,input_text[1].split(' ')))
        sets = {}
        fives = []
        sixes = []
        for signal in signals:
            if len(signal) in lenmap: #1,4,7,8
                sets[lenmap[len(signal)]] = set(signal)
            elif len(signal) == 5: #2, 3, 5:
                fives.append(set(signal))
            elif len(signal) == 6: #6,9,0
                sixes.append(set(signal))
        # print("filter", list(filter(lambda x:len(set(x).difference(sets[1]))==3,fives)))

        sets[2] = list(filter(lambda x:len(x.difference(sets[4]))==3,fives))[0]
        sets[3] = list(filter(lambda x:len(x.difference(sets[1]))==3,fives))[0]
        sets[6] = list(filter(lambda x:len(x.difference(sets[1]))==5,sixes))[0]
        sets[9] = list(filter(lambda x:len(x.intersection(sets[4]))==4,sixes))[0]
        sets[5] = list(filter(lambda x:x.issubset(sets[9]) and x != sets[3],fives))[0]
        sets[0] = list(filter(lambda x:len(x.intersection(sets[4]))==3 and len(x.intersection(sets[1]))==2,sixes))[0]
        num = []
        for output in outputs:
            for i in range(10):
                if sets[i] == set(output):
                    num.append(i)
                    break
        print("num: ", num)
        nums.append(convertlistofints(num))
    print("sum: ", sum(nums))
                
        # print(sets)

