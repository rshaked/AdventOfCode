
from collections import Counter

def gammaepsilon(lines):

    gamma = 0
    eps = 0
    onesandzeroes = {}
    for i in range(len(lines[0].strip())):
        onesandzeroes[i] = dict(Counter([line.strip()[i] for line in lines]))
    print(onesandzeroes)

    for i in range(len(lines[0].strip())):
        if onesandzeroes[i]['0'] > onesandzeroes[i]['1']:
            gamma = gamma*10 + 0
            eps = eps*10 + 1
        else:
            gamma = gamma*10 + 1
            eps = eps*10 + 0
    
    print(gamma)
    print(eps)
    return str(gamma), str(eps)
    

inputfile = open("input.txt", 'r')
lines = inputfile.readlines()

gamma, epsilon = gammaepsilon(lines)
print(gamma, epsilon)
print(int(gamma, 2)*int(epsilon,2))