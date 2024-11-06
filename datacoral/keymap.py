kmap = { '1': ['a', 'b', 'c'],
         '2': ['d', 'e'],
         '3': ['f', 'g', 'h']
         }

def genP(inD, exWords):
    nLetters = kmap[inD]
    newWords = []
    for letter in nLetters:
        for w in exWords:
            newW = letter + w
            newWords.append(newW)
    return newWords


def getAllCombinations(inDigits):
    cWords = ['']
    for d in inDigits[::-1]:
        cWords = genP(d, cWords)
    print cWords


getAllCombinations('213')
