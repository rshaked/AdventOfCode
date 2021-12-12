from collections import Counter


def oxratings(lines):
    linesleft = lines

    for i in range(len(lines[0].strip())):
        onesandzeroes = Counter([line.strip()[i] for line in linesleft])
        print(onesandzeroes)
        if onesandzeroes['0'] > onesandzeroes['1']:
            linesleft = [line.strip() for line in linesleft if line.strip()[i] == '0']
        else: 
            linesleft = [line.strip() for line in linesleft if line.strip()[i] == '1']
        # print(linesleft)
        if len(linesleft) == 1:
            print(linesleft)
            return linesleft[0]


def scrubratings(lines):
    linesleft = lines

    for i in range(len(lines[0].strip())):
        onesandzeroes = Counter([line.strip()[i] for line in linesleft])
        print(onesandzeroes)
        if onesandzeroes['0'] <= onesandzeroes['1']:
            linesleft = [line.strip() for line in linesleft if line.strip()[i] == '0']
        else: 
            linesleft = [line.strip() for line in linesleft if line.strip()[i] == '1']
        # print(linesleft)
        if len(linesleft) == 1:
            print(linesleft)
            return linesleft[0]
    

inputfile = open("input.txt", 'r')
lines = inputfile.readlines()
o = oxratings(lines)
s = scrubratings(lines)
print(o,s)
print(int(o,2), int(s,2))
print(int(o,2) * int(s,2))